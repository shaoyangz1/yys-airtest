import argparse

from airtest.core.api import *
from airtest.utils.logger import get_logger
from page import SoulPage, RankPage
from page.activity import ActivityPage
from page.material import MaterialPage
from settings import settings

logger = get_logger("airtest")
logger.setLevel(settings.LOGLEVEL)  # airtest日志级别
init_device(platform="Android", uuid=settings.UUID)


def soul1_team():
    """御魂"""
    page = SoulPage()
    page.start_soul1_team(times=100)


def soul1_member():
    """御魂"""
    page = SoulPage()
    page.start_soul1_team(times=100)


def soul2():
    """业原火"""
    page = SoulPage()
    page.start_soul2(times=100)


def rank():
    """斗技"""
    page = RankPage()
    page.start_rank(times=30)


def material():
    """觉醒材料"""
    page = MaterialPage()
    for m_type in [2]:  # 改类型
        page.enter_material()
        page.collect_material(m_type=m_type, times=10)  # 改次数
        page.quit_material()


def activity():
    """活动"""
    page = ActivityPage()
    page.start_activity(times=30)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="soul||rank||material||activity", type=str, default="soul")
    args = parser.parse_args()
    globals()[args.type]()
