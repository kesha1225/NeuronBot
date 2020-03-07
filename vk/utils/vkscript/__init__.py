import vk.utils.vkscript.handlers.assignments
import vk.utils.vkscript.handlers.blocks
import vk.utils.vkscript.handlers.calls
import vk.utils.vkscript.handlers.expressions
import vk.utils.vkscript.handlers.statements
import vk.utils.vkscript.handlers.types
from .converter import VKScriptConverter
from .execute import Execute
from .execute import execute


__all__ = ("execute", "Execute", "VKScriptConverter")
