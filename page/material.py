from typing import Literal

from pydantic.main import BaseModel
from airtest.core.api import *

from settings import settings, logger

_PATH = settings.ROOT.joinpath("static/template/material")


class _Elements(BaseModel):
    """图像模版"""

    entry_tpl = Template(_PATH.joinpath("material_icon.png"))
    wheel_tpl = Template(_PATH.joinpath("wheel_material.png"))
    symbol_tpl = Template(_PATH.joinpath("symbol_material.png"))
    carp_tpl = Template(_PATH.joinpath("carp_material.png"))
    drum_tpl = Template(_PATH.joinpath("drum_material.png"))
    fight_tpl = Template(_PATH.joinpath("fight_icon.png"))
    prepare_tpl = Template(_PATH.joinpath("prepare_icon.png"))
    reward_tpl = Template(_PATH.joinpath("reward_icon.png"))
    back_tpl = Template(_PATH.joinpath("back_icon.png"))
    level_ten_tpl = Template(_PATH.joinpath("level_ten.png"))

    class Config:
        arbitrary_types_allowed = True
        ignored_types = (Template,)


class MaterialPage:
    """觉醒材料"""

    _elements = _Elements()

    def enter_material(self):
        """进入觉醒材料"""
        logger.info("进入觉醒材料"), touch(self._elements.entry_tpl)

    def quit_material(self):
        """退出觉醒材料"""
        logger.info("退出觉醒材料"), click(self._elements.back_tpl)

    def select_material(self, m_type: int = Literal[1, 2, 3, 4]):
        """选择觉醒材料"""
        if m_type == 1:
            logger.info("选择挑战火麒麟"), click(self._elements.wheel_tpl)
        elif m_type == 2:
            logger.info("选择挑战风麒麟"), click(self._elements.symbol_tpl)
        elif m_type == 3:
            logger.info("选择挑战水麒麟"), click(self._elements.carp_tpl)
        else:
            logger.info("选择挑战雷麒麟"), click(self._elements.drum_tpl)
        logger.info("滑动层数"), swipe((300, 900), (300, 200))
        time.sleep(1)  # 过度动画
        logger.info("选择挑战十层"), click(self._elements.level_ten_tpl)

    def collect_material(self, times: int = 10):
        """
        收集觉醒材料
        :param times: 挑战次数
        """
        while times > 0:
            logger.info("开始挑战"), click(self._elements.fight_tpl)
            time.sleep(5)  # 过度动画
            count = 60
            while count > 0:
                #  战斗180s 没结束就投降
                try:
                    loop_find(self._elements.reward_tpl, timeout=3)
                    time.sleep(2)  # 过度动画
                    logger.info("领取奖励"), click(self._elements.reward_tpl)
                    break
                except TargetNotFoundError:
                    count -= 1
            times -= 1


if __name__ == "__main__":
    page = MaterialPage()
    times = 10  # 改次数
    for m_type in [1, 2, 3, 4]:  # 改类型
        page.enter_material()
        page.select_material(m_type=m_type)
        page.collect_material(times=times)
        time.sleep(2)  # 过度动画
        page.quit_material()
