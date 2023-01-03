from typing import Literal

from pydantic.main import BaseModel
from airtest.core.api import *

from settings import settings, logger

_PATH = "static/template/material"


class _Elements(BaseModel):
    """图像模版"""

    entry_tpl = Template(settings.ROOT.joinpath(_PATH, "material_icon.png"))
    wheel_tpl = Template(settings.ROOT.joinpath(_PATH, "wheel_material.png"))
    symbol_tpl = Template(settings.ROOT.joinpath(_PATH, "symbol_material.png"))
    carp_tpl = Template(settings.ROOT.joinpath(_PATH, "carp_material.png"))
    drum_tpl = Template(settings.ROOT.joinpath(_PATH, "drum_material.png"))
    fight_tpl = Template(settings.ROOT.joinpath(_PATH, "fight_icon.png"))
    prepare_tpl = Template(settings.ROOT.joinpath(_PATH, "prepare_icon.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward_icon.png"))
    back_tpl = Template(settings.ROOT.joinpath(_PATH, "back_icon.png"))

    class Config:
        arbitrary_types_allowed = True


class MaterialPage:
    """觉醒材料"""

    _elements = _Elements()

    def enter_material(self):
        """进入觉醒材料"""
        logger.info("进入觉醒材料"), click(self._elements.entry_tpl)

    def quit_material(self):
        """退出觉醒材料"""
        logger.info("退出觉醒材料"), click(self._elements.back_tpl)

    def collect_material(self, m_type: int, times: int = 10):
        """
        收集觉醒材料
        :param m_type: 材料类型： 1，2，3，4
        :param times: 挑战次数
        """
        while times > 0:
            if m_type == 1:
                logger.info("挑战火麒麟"), click(self._elements.wheel_tpl)
            elif m_type == 2:
                logger.info("挑战风麒麟"), click(self._elements.symbol_tpl)
            elif m_type == 3:
                logger.info("挑战水麒麟"), click(self._elements.carp_tpl)
            else:
                logger.info("挑战雷麒麟"), click(self._elements.drum_tpl)
            logger.info("开始挑战"), click(self._elements.fight_tpl)
            time.sleep(2)  # 过度动画
            if exists(self._elements.prepare_tpl):
                logger.info("点击准备"), click(self._elements.prepare_tpl)
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
