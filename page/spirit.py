from typing import Literal

from airtest.core.api import *
from pydantic.main import BaseModel
from settings import settings, logger

_PATH = "static/template/spirit"


class _Elements(BaseModel):
    """首页元素"""

    entry_tpl = Template(settings.ROOT.joinpath(_PATH, "soul_icon.png"))
    prepare_tpl = Template(settings.ROOT.joinpath(_PATH, "prepare_icon.png"))
    solo_tpl = Template(settings.ROOT.joinpath(_PATH, "solo_icon.png"))
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
        ignored_types = (Template,)


class SpiritPage:
    """御魂"""

    def __init__(self):
        self._elements = _Elements()

    def spirit1_solo(self, times: int = 100):
        """魂土单人"""
        count = 0
        while count < times:
            count += 1
            touch(self._elements.solo_tpl), logger.info(f"第{count}次挑战魂土")
            time.sleep(15), wait(self._elements.complete1_tpl, timeout=50)
            logger.info("战斗结束"), touch(self._elements.complete1_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(0.5), logger.info("领取奖励")
            touch(self._elements.reward_tpl), time.sleep(0.5)

    def spirit1_team(self, times: int = 100):
        """魂土队长"""
        count = 0
        while count < times:
            count += 1
            while exists(self._elements.battle1_tpl):
                logger.info("组队中")
                touch(self._elements.battle1_tpl), time.sleep(3)
            logger.info(f"第{count}次挑战魂土")
            time.sleep(15), wait(self._elements.complete1_tpl, timeout=50)
            logger.info("战斗结束"), touch(self._elements.complete1_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(0.5), logger.info("领取奖励")
            touch(self._elements.reward_tpl), time.sleep(0.5)

    def spirit1_member(self, times: int = 100):
        """魂土队员"""
        count = 0
        while count < times:
            count += 1
            logger.info(f"第{count}次挑战魂土")
            time.sleep(15), wait(self._elements.complete1_tpl, timeout=50)
            logger.info("战斗结束"), touch(self._elements.complete1_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(0.5), logger.info("领取奖励")
            touch(self._elements.reward_tpl), time.sleep(0.5)

    def spirit_by_type(self, s_type: int = Literal[2, 3, 4], times: int = 10):
        """御魂挑战
        :type s_type: 御魂类型
        :type times: 挑战次数
        """
        count = 0
        while count < times:
            count += 1
            if s_type == 2:
                logger.info(f"第{count}次挑战痴之阵"), touch(self._elements.type2_tpl)
                touch(self._elements.battle2_tpl)
            else:
                logger.info(f"第{count}次挑战日轮之陨"), touch(self._elements.type3_tpl)
                touch(self._elements.battle3_tpl)
            logger.info("开始战斗"), time.sleep(10)
            logger.info("等待战斗结束"), wait(self._elements.complete2_tpl, timeout=20)
            logger.info("战斗结束"), touch(self._elements.complete2_tpl)
            wait(self._elements.reward_tpl, timeout=30)
            logger.info("等待奖励刷新"), time.sleep(1)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)

    def sprite_fight(self, times: int = 10):
        """御灵"""
        count = 0
        while count < times:
            count += 1
            logger.info(f"第{count}次挑战御灵"), touch(self._elements.battle3_tpl)
            logger.info("开始战斗"), time.sleep(10)
            wait(self._elements.reward_tpl, timeout=60)
            logger.info("等待奖励刷新"), time.sleep(1)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)
