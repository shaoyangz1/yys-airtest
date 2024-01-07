from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger
from airtest.core import api

__all__ = [
    "spirit1_solo",
    "spirit1_team",
    "spirit1_member",
    "spirit2",
    "spirit3",
    "spirit4",
]

_PATH = settings.ROOT.joinpath("static/template/spirit")


class _Elements(BaseModel):
    """首页元素"""

    battle1_solo = Template(_PATH.joinpath("battle1_solo.png"))
    battle1_duo = Template(_PATH.joinpath("battle1_duo.png"))
    complete1 = Template(_PATH.joinpath("complete1.png"))
    battle2 = Template(_PATH.joinpath("battle2.png"))
    complete2 = Template(_PATH.joinpath("complete2.png"))
    battle3 = Template(_PATH.joinpath("battle3.png"))
    complete3 = Template(_PATH.joinpath("complete3.png"))
    battle4 = Template(_PATH.joinpath("battle4.png"))
    reward = Template(_PATH.joinpath("reward.png"))

    class Config:
        arbitrary_types_allowed = True
        ignored_types = (Template,)


_elements = _Elements()


def spirit1_solo(times: int = 100):
    """魂土单人"""
    count = 0
    while count < times:
        count += 1
        logger.info(f"第{count}次挑战魂土"), touch(_elements.battle1_solo)
        time.sleep(15), wait(_elements.complete1, timeout=50)
        logger.info("战斗结束"), touch(_elements.complete1)
        wait(_elements.reward, timeout=30)
        time.sleep(0.5), logger.info("领取奖励")
        touch(_elements.reward), time.sleep(0.5)


def spirit1_team(times: int = 100):
    """魂土队长"""
    count = 0
    while count < times:
        count += 1
        while exists(_elements.battle1_duo):
            logger.info("组队中")
            touch(_elements.battle1), time.sleep(3)
        logger.info(f"第{count}次挑战魂土")
        time.sleep(15), wait(_elements.complete1, timeout=50)
        logger.info("战斗结束"), touch(_elements.complete1)
        wait(_elements.reward, timeout=30)
        time.sleep(0.5), logger.info("领取奖励")
        touch(_elements.reward), time.sleep(0.5)


def spirit1_member(times: int = 100):
    """魂土队员"""
    count = 0
    while count < times:
        count += 1
        logger.info(f"第{count}次挑战魂土")
        wait(_elements.reward, timeout=60)
        time.sleep(0.5), logger.info("领取奖励")
        touch(_elements.reward), time.sleep(0.5)


def spirit2(times: int = 10):
    """业原火"""
    count = 0
    while count < times:
        count += 1
        logger.info(f"第{count}次挑战痴之阵"), touch(_elements.battle2)
        logger.info("开始战斗"), time.sleep(30)
        logger.info("等待战斗结束"), wait(_elements.complete2, timeout=60)
        logger.info("战斗结束"), touch(_elements.complete2)
        wait(_elements.reward, timeout=30)
        logger.info("等待奖励刷新"), time.sleep(0.5)
        logger.info("领取奖励"), touch(_elements.reward)


def spirit3(times: int = 10):
    """日轮之陨"""
    count = 0
    while count < times:
        count += 1
        logger.info(f"第{count}次挑战日轮之陨"), touch(_elements.battle3)
        logger.info("开始战斗"), time.sleep(10)
        logger.info("等待战斗结束"), wait(_elements.complete3, timeout=60)
        logger.info("战斗结束"), touch(_elements.complete3)
        wait(_elements.reward, timeout=30)
        logger.info("等待奖励刷新"), time.sleep(0.5)
        logger.info("领取奖励"), touch(_elements.reward)


def spirit4(times: int = 10):
    """御灵"""
    count = 0
    while count < times:
        count += 1
        logger.info(f"第{count}次挑战御灵"), touch(_elements.battle4)
        logger.info("开始战斗"), time.sleep(10)
        wait(_elements.reward, timeout=60)
        logger.info("等待奖励刷新"), time.sleep(1)
        logger.info("领取奖励"), touch(_elements.reward)


if __name__ == "__main__":
    spirit4(times=50)
