from typing import TYPE_CHECKING

from vk.methods import Account
from vk.methods import Apps
from vk.methods import AppWidgets
from vk.methods import Auth
from vk.methods import Board
from vk.methods import Database
from vk.methods import Docs
from vk.methods import Fave
from vk.methods import Friends
from vk.methods import Gifts
from vk.methods import Groups
from vk.methods import Leads
from vk.methods import Likes
from vk.methods import Market
from vk.methods import Messages
from vk.methods import Status
from vk.utils import ContextInstanceMixin

if TYPE_CHECKING:
    from vk import VK


class API(ContextInstanceMixin):
    def __init__(self, vk: "VK"):
        self.vk = vk

        self.account = Account(vk, category="account")
        self.messages = Messages(vk, category="messages")
        self.apps = Apps(vk, category="apps")
        self.appwidgets = AppWidgets(vk, category="appWidgets")
        self.auth = Auth(vk, category="auth")
        self.board = Board(vk, category="board")
        self.database = Database(vk, category="database")
        self.docs = Docs(vk, category="docs")
        self.fave = Fave(vk, category="fave")
        self.friends = Friends(vk, category="friends")
        self.gifts = Gifts(vk, category="gifts")
        self.groups = Groups(vk, category="groups")
        self.leads = Leads(vk, category="leads")
        self.likes = Likes(vk, category="likes")
        self.market = Market(vk, category="market")
        self.status = Status(vk, category="status")
