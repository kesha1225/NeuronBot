"""
VK bot framework, easily to learn, fast to code, built on vk.py.
Designed specially for heavy loads.
"""
from .dispatcher import Dispatcher
from .dispatcher.dispatcher import get_group_id
from .dispatcher.handler import SkipHandler
from .dispatcher.storage import Storage, AsyncStorage
from .middlewares.middlewares import BaseMiddleware
from .rules import rules
from .rules.rules import BaseRule
from .rules.rules import NamedRule
