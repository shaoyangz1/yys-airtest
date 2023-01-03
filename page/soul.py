import time

from pydantic.main import BaseModel
from airtest.core.api import *

from settings import settings, logger

_PATH = "static/template/soul"


class _Elements(BaseModel):
    """首页元素"""

    entry_tpl = Template(settings.ROOT.joinpath(_PATH, "soul_icon.png"))
    prepare_tpl = Template(settings.ROOT.joinpath(_PATH, "prepare_icon.png"))
    battle1_tpl = Template(settings.ROOT.joinpath(_PATH, "battle2_icon.png"))
    complete1_tpl = Template(settings.ROOT.joinpath(_PATH, "complete2_icon.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward_icon.png"))
    battle2_tpl = Template(settings.ROOT.joinpath(_PATH, "battle2_icon.png"))
    complete2_tpl = Template(settings.ROOT.joinpath(_PATH, "complete2_icon.png"))

    class Config:
        arbitrary_types_allowed = True


class SoulPage:
    """御魂"""

    _elements = _Elements()

    def enter_soul(self):
        """进入御魂界面"""
        click(self._elements.entry_tpl)

    def start_soul1_team(self, times: int = 100):
        """御魂挑战 1 八岐大蛇
        :type times: 挑战次数
        """
        while times > 0:
            logger.info("挑战魂土"), click(self._elements.battle1_tpl)
            time.sleep(10)
            wait(self._elements.complete1_tpl, timeout=50)
            logger.info("战斗结束"), click(self._elements.complete1_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(3)
            logger.info("领取奖励"), click(self._elements.reward_tpl)
            times -= 1
            time.sleep(2)

    def start_soul1_member(self, times: int = 100):
        """御魂挑战 1 八岐大蛇
        :type times: 挑战次数
        """
        while times > 0:
            logger.info("挑战魂土")
            time.sleep(10)
            wait(self._elements.complete1_tpl, timeout=50)
            logger.info("战斗结束"), click(self._elements.complete1_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(3)
            logger.info("领取奖励"), click(self._elements.reward_tpl)
            times -= 1
            time.sleep(2)

    def start_soul2(self, times: int = 10):
        """御魂挑战 2 业原火
        :type times: 挑战次数
        """
        while times > 0:
            logger.info("挑战痴之阵"), click(self._elements.battle2_tpl)
            time.sleep(5)
            if exists(self._elements.prepare_tpl):
                logger.info("点击准备"), click(self._elements.prepare_tpl)
            logger.info("准备完毕开始战斗"), time.sleep(60)
            wait(self._elements.complete2_tpl, timeout=120)
            logger.info("业原火战斗结束"), click(self._elements.complete2_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(3)
            logger.info("领取奖励"), click(self._elements.reward_tpl)
            times -= 1
            time.sleep(2)
