from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger

_PATH = "static/template/activity"


class _Elements(BaseModel):
    """图像模版"""

    challenge_tpl = Template(settings.ROOT.joinpath(_PATH, "challenge.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward.png"))

    class Config:
        arbitrary_types_allowed = True


class ActivityPage:
    def __init__(self):
        self._elements = _Elements()

    def start(self, times: int = 100):
        while times > 0:
            touch(self._elements.challenge_tpl)
            logger.info("开始挑战"), time.sleep(10)
            wait(self._elements.reward_tpl, timeout=20)
            time.sleep(2)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)
            times -= 1
            time.sleep(2)
