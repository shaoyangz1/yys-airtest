from typing import Literal

from airtest.core.api import *
from pydantic.main import BaseModel
from settings import settings, logger

_PATH = "static/template/spirit"


class _Elements(BaseModel):
    """首页元素"""

    entry_tpl = Template(settings.ROOT.joinpath(_PATH, "soul_icon.png"))
    prepare_tpl = Template(settings.ROOT.joinpath(_PATH, "prepare_icon.png"))
    battle1_tpl = Template(settings.ROOT.joinpath(_PATH, "battle1_icon.png"))
    complete1_tpl = Template(settings.ROOT.joinpath(_PATH, "complete1_icon.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward_icon1.png"))
    battle2_tpl = Template(settings.ROOT.joinpath(_PATH, "battle2_icon.png"))
    type2_tpl = Template(settings.ROOT.joinpath(_PATH, "battle2_type.png"))
    complete2_tpl = Template(settings.ROOT.joinpath(_PATH, "complete2_icon.png"))
    battle3_tpl = Template(settings.ROOT.joinpath(_PATH, "battle3_icon.png"))
    type3_tpl = Template(settings.ROOT.joinpath(_PATH, "battle3_type.png"))
    battle4_tpl = Template(settings.ROOT.joinpath(_PATH, "battle4_icon.png"))

    class Config:
        arbitrary_types_allowed = True


class SpiritPage:
    """御魂"""

    def __init__(self):
        self._elements = _Elements()

    def enter_spirit(self):
        """进入御魂界面"""
        touch(self._elements.entry_tpl)

    def start_spirit1_team(self, times: int = 100):
        """御魂挑战 1 八岐大蛇
        :type times: 挑战次数
        """
        while times > 0:
            while exists(self._elements.battle1_tpl):
                logger.info("组队中"), touch(self._elements.battle1_tpl)
                time.sleep(3)
            logger.info("挑战魂土")
            time.sleep(10)
            wait(self._elements.complete1_tpl, timeout=50)
            logger.info("战斗结束"), touch(self._elements.complete1_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(3)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)
            times -= 1

    def start_spirit1_member(self, times: int = 100):
        """御魂挑战 1 八岐大蛇
        :type times: 挑战次数
        """
        while times > 0:
            logger.info("挑战魂土")
            time.sleep(10)
            wait(self._elements.complete1_tpl, timeout=50)
            logger.info("战斗结束"), touch(self._elements.complete1_tpl)
            wait(self._elements.reward_tpl, timeout=50)
            time.sleep(3)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)
            times -= 1
            time.sleep(2)

    def start_spirit_by_type(self, s_type: int = Literal[2, 3, 4], times: int = 10):
        """御魂挑战
        :type s_type: 御魂类型
        :type times: 挑战次数
        """
        while times > 0:
            if s_type == 2:
                logger.info("挑战痴之阵"), touch(self._elements.type2_tpl)
                touch(self._elements.battle2_tpl)
            else:
                logger.info("挑战日轮之陨"), touch(self._elements.type3_tpl)
                touch(self._elements.battle3_tpl)
            time.sleep(10)
            if exists(self._elements.prepare_tpl):
                logger.info("点击准备"), touch(self._elements.prepare_tpl)
            logger.info("准备完毕开始战斗"), time.sleep(60)
            wait(self._elements.complete2_tpl, timeout=120)
            logger.info("战斗结束"), touch(self._elements.complete2_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(3)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)
            times -= 1
            time.sleep(2)

    def sprite_fight(self, times: int = 10):
        """御灵"""
        while times > 0:
            touch(self._elements.battle3_tpl)
            logger.info("准备完毕开始战斗"), time.sleep(60)
            wait(self._elements.reward_tpl, timeout=60)
            time.sleep(5)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)
            times -= 1
            time.sleep(2)
