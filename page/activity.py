from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger

_PATH = "static/template/activity"


class _Elements(BaseModel):
    """图像模版"""

    challenge_tpl = Template(settings.ROOT.joinpath(_PATH, "challenge.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward.png"))
    continue_tpl = Template(settings.ROOT.joinpath(_PATH, "continue.png"))

    class Config:
        arbitrary_types_allowed = True


class ActivityPage:
    def __init__(self):
        self._elements = _Elements()

    def start(self, times: int = 100):
        count = 0
        while count < times:
            count += 1
            touch(self._elements.challenge_tpl)
            logger.info(f"开始第{count}次挑战"), time.sleep(5)
            wait(self._elements.reward_tpl, timeout=30)
            time.sleep(.5)
            logger.info("领取奖励"), touch(self._elements.reward_tpl)
            time.sleep(1)
