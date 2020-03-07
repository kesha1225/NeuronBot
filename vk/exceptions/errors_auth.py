import typing
from urllib.parse import urlencode


class VkException(Exception):
    pass


class VkAuthError(VkException):
    def __init__(
        self, error, description, url: str = "", params: typing.Any = ""
    ):
        self.error = error
        self.description = description
        self.url = "{}?{}".format(url, urlencode(params))

    def __str__(self):
        return self.description


class VkCaptchaNeeded(VkException):
    def __init__(self, url, sid):
        self.url = url
        self.sid = sid

    def __str__(self):
        return "You must enter the captcha"


class VkTwoFactorCodeNeeded(VkException):
    def __str__(self):
        return (
            "In order to confirm that you are the owner of this page "
            "please enter the code provided by the code generating app."
        )