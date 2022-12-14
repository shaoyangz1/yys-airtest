import argparse

from airtest.core.api import *
from airtest.utils.logger import get_logger

from page import SpiritPage, RankPage
from page.material import MaterialPage
from page.ward import WardPage
from settings import settings

logger = get_logger("airtest")
logger.setLevel(settings.LOGLEVEL)  # airtest日志级别
init_device(platform="Android", uuid=settings.UUID)


def spirit1_team():
    """御魂"""
    page = SpiritPage()
    page.start_spirit1_team(times=10000)


def spirit1_member():
    """御魂"""
    page = SpiritPage()
    page.start_spirit1_member(times=10000)


def spirit2():
    """业原火"""
    page = SpiritPage()
    page.start_spirit_by_type(s_type=2, times=70)


def spirit3():
    """日冕之轮"""
    page = SpiritPage()
    page.start_spirit_by_type(s_type=3, times=70)


def rank():
    """斗技"""
    page = RankPage()
    page.start_rank(times=30)


def material():
    """觉醒材料"""
    page = MaterialPage()
    times = 1  # 改次数
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        help="spirit||rank||material",
        type=str,
        default="spirit",
    )
    args = parser.parse_args()
    globals()[args.type]()
