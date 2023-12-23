import argparse

from airtest.core.api import *
from airtest.utils.logger import get_logger

from page import SpiritPage, RankPage, ActivityPage
from page.material import MaterialPage
from page.ward import WardPage
from settings import settings

logger = get_logger("airtest")
logger.setLevel(settings.LOGLEVEL)  # airtest日志级别


def spirit_solo():
    """御魂单人"""
    page = SpiritPage()
    page.spirit1_solo(times=120)


def spirit1_team():
    """御魂队长"""
    page = SpiritPage()
    page.spirit1_team(times=10000)


def spirit1_member():
    """御魂队友"""
    page = SpiritPage()
    page.spirit1_member(times=10000)


def spirit2():
    """业原火"""
    page = SpiritPage()
    page.spirit_by_type(s_type=2, times=50)


def spirit3():
    """日轮之陨"""
    page = SpiritPage()
    page.spirit_by_type(s_type=3, times=49)


def rank():
    """斗技"""
    page = RankPage()
    page.start_rank(times=30)


def activity():
    """限时活动"""
    page = ActivityPage()
    page.start(times=1000)


def material():
    """觉醒材料"""
    page = MaterialPage()
    times = 50  # 改次数
    for m_type in [1, 2, 3, 4]:  # 改类型
        page.enter_material()
        page.select_material(m_type=m_type)
        page.collect_material(times=times)
        time.sleep(2)  # 过度动画
        page.quit_material()


def ward():
    """结界突破"""
    page = WardPage()
    page.surrender_wards(nums=9)


def sprite():
    """御灵"""
    page = SpiritPage()
    page.sprite_fight(times=69)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        help="spirit||rank||material",
        type=str,
        default="spirit3",
    )
    parser.add_argument(
        "--device",
        help="uuid",
        type=str, 
        default=settings.UUID,
    )
    args = parser.parse_args()
    init_device(platform="Android", uuid=args.device)
    globals()[args.type]()
