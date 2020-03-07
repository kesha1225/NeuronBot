"""
Author: https://github.com/Fahreeve/aiovk/blob/master/aiovk/sessions.py
"""
from urllib.parse import parse_qsl, urljoin
import typing
from html.parser import HTMLParser

import aiohttp
from yarl import URL

from vk.exceptions import VkAuthError, VkTwoFactorCodeNeeded, VkCaptchaNeeded
from vk.constants import JSON_LIBRARY


class AuthPageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.url = None
        self.message = None
        self.recording = None
        self.captcha_url = None

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            attrs = dict(attrs)
            if attrs["type"] != "submit":
                self.inputs.append((attrs["name"], attrs.get("value", "")))
        elif tag == "form":
            for name, value in attrs:
                if name == "action":
                    self.url = value
        elif tag == "img":
            attrs = dict(attrs)
            if attrs.get("class", "") == "captcha_img":
                self.captcha_url = attrs["src"]
        elif tag == "div":
            attrs = dict(attrs)
            if attrs.get("class", "") == "service_msg service_msg_warning":
                self.recording = 1

    def handle_endtag(self, tag):
        if tag == "div":
            self.recording = 0

    def handle_data(self, data):
        if self.recording:
            self.message = data


class TwoFactorCodePageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.url = None
        self.message = None
        self.recording = None

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            attrs = dict(attrs)
            if attrs["type"] != "submit":
                self.inputs.append((attrs["name"], attrs.get("value", "")))
        elif tag == "form":
            for name, value in attrs:
                if name == "action":
                    self.url = urljoin("https://m.vk.com/", value)
        elif tag == "div":
            attrs = dict(attrs)
            if attrs.get("class", "") == "service_msg service_msg_warning":
                self.recording = 1

    def handle_endtag(self, tag):
        if tag == "div":
            self.recording = 0

    def handle_data(self, data):
        if self.recording:
            self.message += data


class AccessPageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.url = None

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            attrs = dict(attrs)
            if attrs["type"] != "submit":
                self.inputs.append((attrs["name"], attrs.get("value", "")))
        elif tag == "form":
            for name, value in attrs:
                if name == "action":
                    self.url = value


class AuthManager:
    """
    For client authorization in js apps and standalone (desktop and mobile) apps
    See more in https://new.vk.com/dev/implicit_flow_user
    """

    AUTH_URL = "https://oauth.vk.com/authorize"
    API_VERSION = "5.103"

    def __init__(
        self,
        login: str,
        password: str,
        app_id: int = 2685278,
        scope: typing.Union[str, int, list] = None,
        num_of_attempts: int = 5,
    ):
        """
        :param login: user login
        :param password: user password
        :param app_id: application id. More details in `Application registration` block in `https://vk.com/dev/first_guide`
        :param scope: access rights. See `Access rights` block in `https://vk.com/dev/first_guide`
        :param num_of_attempts: number of authorization attempts
        """

        self.login = login
        self.password = password
        self.app_id = app_id
        self.num_of_attempts = num_of_attempts
        self._access_token = None
        self.session = aiohttp.ClientSession()
        if isinstance(scope, (str, int, type(None))):
            self.scope = scope
        elif isinstance(scope, list):
            self.scope = ",".join(scope)

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    async def authorize(self) -> None:
        """Getting a new token from server"""
        html = await self._get_auth_page()
        url = URL("/authorize?email")
        for _ in range(self.num_of_attempts):
            if url.path == "/authorize" and "email" in url.query:
                url, html = await self._process_auth_form(html)
            if (
                url.path == "/login"
                and url.query.get("act", "") == "authcheck"
            ):
                url, html = await self._process_2auth_form(html)
            if (
                url.path == "/login"
                and url.query.get("act", "") == "authcheck_code"
            ):
                url, html = await self._process_auth_form(html)
            if url.path == "/authorize" and "__q_hash" in url.query:
                url, html = await self._process_access_form(html)
            if url.path == "/blank.html":
                parsed_fragments = dict(parse_qsl(url.fragment))
                self.access_token = parsed_fragments["access_token"]
                await self.session.close()
                return None
        raise VkAuthError(
            "Something went wrong", "Exceeded the number of attempts to log in"
        )

    async def _get_auth_page(self) -> str:
        """
        Get authorization mobile page without js
        :return: html page
        """
        params = {
            "client_id": self.app_id,
            "redirect_uri": "https://oauth.vk.com/blank.html",
            "display": "mobile",
            "response_type": "token",
            "v": self.API_VERSION,
        }
        if self.scope:
            params["scope"] = self.scope

        async with self.session.get(url=self.AUTH_URL, params=params) as resp:
            response = await resp.text()
            status = resp.status

        if status != 200:
            error_dict = JSON_LIBRARY.loads(response)
            raise VkAuthError(
                error_dict["error"],
                error_dict["error_description"],
                self.AUTH_URL,
                params,
            )
        return response

    async def _get_data_from_form(self, form_url: str, form_data: dict):
        async with self.session.post(url=form_url, data=form_data) as resp:
            return resp.real_url, await resp.text()

    async def _process_auth_form(self, html: str) -> typing.Tuple[URL, str]:
        """
        Parsing data from authorization page and filling the form and submitting the form

        :param html: html page
        :return: url and  html from redirected page
        """
        parser = AuthPageParser()
        parser.feed(html)
        parser.close()

        form_data = dict(parser.inputs)
        form_url = parser.url
        form_data["email"] = self.login
        form_data["pass"] = self.password
        if parser.message:
            raise VkAuthError(
                "invalid_data", parser.message, form_url, form_data
            )
        if parser.captcha_url:
            form_data["captcha_key"] = await self.enter_captcha(
                "https://m.vk.com{}".format(parser.captcha_url),
                form_data["captcha_sid"],
            )
            form_url = "https://m.vk.com{}".format(form_url)

        url, html = await self._get_data_from_form(form_url, form_data)
        return url, html

    async def _process_2auth_form(self, html: str) -> typing.Tuple[URL, str]:
        """
        Parsing two-factor authorization page and filling the code

        :param html: html page
        :return: url and  html from redirected page
        """
        parser = TwoFactorCodePageParser()
        parser.feed(html)
        parser.close()

        form_url = parser.url
        form_data = dict(parser.inputs)
        form_data["remember"] = 0
        if parser.message:
            raise VkAuthError("invalid_data", parser.message, form_url, form_data)
        form_data["code"] = await self.enter_confirmation_code()

        url, html = await self._get_data_from_form(form_url, form_data)
        return url, html

    async def _process_access_form(self, html: str) -> typing.Tuple[URL, str]:
        """
        Parsing page with access rights

        :param html: html page
        :return: url and  html from redirected page
        """
        parser = AccessPageParser()
        parser.feed(html)
        parser.close()

        form_url = parser.url
        form_data = dict(parser.inputs)

        url, html = await self._get_data_from_form(form_url, form_data)
        return url, html

    async def enter_confirmation_code(self) -> str:
        """
        Override this method for processing confirmation 2uth code.
        :return confirmation code
        """
        raise VkTwoFactorCodeNeeded()

    async def enter_captcha(self, url: str, sid: str) -> str:
        """
        Override this method for processing captcha.

        :param url: link to captcha image
        :param sid: captcha id. I do not know why pass here but may be useful
        :return captcha value
        """
        raise VkCaptchaNeeded(url, sid)
