from .base import BaseMethod
from vk.types.responses import leads as m


class Leads(BaseMethod):
    async def check_user(
        self,
        lead_id: int = None,
        test_result: int = None,
        test_mode: bool = None,
        auto_start: bool = None,
        age: int = None,
        country: str = None,
    ):
        """
        Check if the user can start the lead.
        :param lead_id: Lead ID.
        :param test_result: Value to be return in 'result' field when test mode is used.
        :param test_mode:
        :param auto_start:
        :param age: User age.
        :param country: User country code.


        """
        method = self.get_method_name(self.check_user)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.CheckUser(**r)

    async def complete(
        self, vk_sid: str = None, secret: str = None, comment: str = None
    ):
        """
        Complete the lead started by user.
        :param vk_sid: Session obtained as GET parameter when session started.
        :param secret: Secret key from the lead testing interface.
        :param comment: Comment text.


        """
        method = self.get_method_name(self.complete)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Complete(**r)

    async def get_stats(
        self,
        lead_id: int = None,
        secret: str = None,
        date_start: str = None,
        date_end: str = None,
    ):
        """
        Return lead stats data.
        :param lead_id: Lead ID.
        :param secret: Secret key obtained from the lead testing interface.
        :param date_start: Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).


        """
        method = self.get_method_name(self.get_stats)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetStats(**r)

    async def get_users(
        self,
        offer_id: int = None,
        secret: str = None,
        offset: int = None,
        count: int = None,
        status: int = None,
        reverse: bool = None,
    ):
        """
        Return a list of last user actions for the offer.
        :param offer_id: Offer ID.
        :param secret: Secret key obtained in the lead testing interface.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param status: Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.


        """
        method = self.get_method_name(self.get_users)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetUsers(**r)

    async def metric_hit(self, data: str = None):
        """
        Count the metric event.
        :param data: Metric data obtained in the lead interface.


        """
        method = self.get_method_name(self.metric_hit)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.MetricHit(**r)

    async def start(
        self,
        lead_id: int = None,
        secret: str = None,
        uid: int = None,
        aid: int = None,
        test_mode: bool = None,
        force: bool = None,
    ):
        """
        Create new session for the user passing the offer.
        :param lead_id: Lead ID.
        :param secret: Secret key from the lead testing interface.
        :param uid:
        :param aid:
        :param test_mode:
        :param force:


        """
        method = self.get_method_name(self.start)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Start(**r)
