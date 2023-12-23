from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger

_PATH = "static/template/battle"


class _Elements(BaseModel):
    """图像模版"""

    prepare_tpl = Template(settings.ROOT.joinpath(_PATH, "prepare_icon.png"))
    back_tpl = Template(settings.ROOT.joinpath(_PATH, "back_icon.png"))
    confirm_tpl = Template(settings.ROOT.joinpath(_PATH, "confirm_icon.png"))
    failure_tpl = Template(settings.ROOT.joinpath(_PATH, "failure_icon.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward_icon.png"))

    class Config:
        arbitrary_types_allowed = True
        ignored_types = (Template,)


class BattlePage:
    def __init__(self):
        self._elements = _Elements()

    def start_battle(self):
        """开始战斗"""
        time.sleep(3)  # 过度动画
        if exists(self._elements.prepare_tpl):
            logger.info("点击准备"), touch(self._elements.confirm_tpl)
        else:
            logger.info("完成准备")

    def quit_battle(self):
        """退出战斗"""
        logger.info("退出战斗"), touch(self._elements.back_tpl)
        logger.info("点击确认"), touch(self._elements.confirm_tpl)
        logger.info("失败结算"), touch(self._elements.failure_tpl)
