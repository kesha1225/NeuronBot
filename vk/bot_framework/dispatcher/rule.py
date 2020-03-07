import logging
from abc import ABC
from abc import abstractmethod

from vk.utils.mixins import MetaMixin

logger = logging.getLogger(__name__)


class AbstractRule(ABC, MetaMixin):
    @abstractmethod
    async def check(self, event, data: dict):
        """
        This method is gonna be called in the rules check.

        :param data:
        :param event:
        :return: True or False. True -> check next rules or execute handler
        """


class BaseRule(AbstractRule, ABC):
    async def __call__(self, event, data: dict) -> bool:
        logger.debug(f"Rule {self.__class__.__name__} succesfully called!")
        return await self.check(event, data)


class NamedRule(BaseRule, ABC):
    """
    Can be added to the list of rules with RuleFactory and
    is going to be called in handlers by unique key;

    >>> @dp.message_handler(unique_key = value)

    """

    key = None  # unique value for access to rule in handlers.
    required = False  # include to all handlers rules.
    default = (
        None
    )  # default value for the rule


class RuleFactory:
    """
    Manage your rules.
    """

    def __init__(self, config: dict):
        self.config = config  # dict of all known rules

    def setup(self, rule: NamedRule):
        """
        Register rule in factory.
        :param rule:
        :return:
        """
        if not issubclass(rule, NamedRule):
            raise RuntimeError("Only NamedRules may be added in rule factory!")

        if rule.key is None or not isinstance(rule.key, str):
            raise RuntimeError("Unallowed key for rule")

        self.config.update({rule.key: rule})
        logger.debug(f"Rule {rule.__class__.__name__} succesfully added!")

    def get_rules(self, user_rules: dict):
        """
        Get rules objects by named_rules.
        :param user_rules:
        :return:
        """
        rules = []
        for key, value in user_rules.items():
            if key in self.config:
                rule: BaseRule = self.config[key](value)
                if rule.meta and rule.meta.get("deprecated", False):
                    logger.warning(
                        f"This rule ({rule.__class__.__name__}) deprecated. Not recommended to use."
                    )
                rules.append(rule)
                continue
            else:
                raise RuntimeError(f"Unknown rule passed: {key}")
        # include required rules
        k: str
        v: NamedRule
        for k, v in self.config.items():
            if v.required:
                this_rule_not_included = True
                for rule in rules:
                    if isinstance(rule, v):
                        this_rule_not_included = False
                        break
                if this_rule_not_included:
                    rules.append(v(v.default))
        return rules
