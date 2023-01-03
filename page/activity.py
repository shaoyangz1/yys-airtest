from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger

_PATH = "static/template/activity"


class _Elements(BaseModel):
    """图像模版"""

    battle_tpl = Template(settings.ROOT.joinpath(_PATH, "battle1_icon.png"))
    complete_tpl = Template(settings.ROOT.joinpath(_PATH, "complete1_icon.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward_icon.png"))

    class Config:
        arbitrary_types_allowed = True


class ActivityPage:
    _elements = _Elements()

    def start_activity(self, times: int = 50):
        """
        开启活动
        :param times: 开启次数
        """
        while times > 0:
            logger.info("开始挑战"), click(self._elements.battle_tpl)
            time.sleep(200)  # 战斗
            wait(self._elements.complete_tpl, timeout=120)  # 等待完成
            logger.info("完成挑战"), click(self._elements.complete_tpl)
            time.sleep(2)  # 过渡动画
            logger.info("领取奖励"), click(self._elements.reward_tpl)
            times -= 1
