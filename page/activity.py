from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger

__all__ = ["start_activity"]

_PATH = settings.ROOT.joinpath("static/template/activity")


class _Elements(BaseModel):
    """图像模版"""

    challenge_tpl = Template(_PATH.joinpath("challenge.png"))
    reward_tpl = Template(_PATH.joinpath("reward.png"))
    continue_tpl = Template(_PATH.joinpath("continue.png"))

    class Config:
        arbitrary_types_allowed = True
        ignored_types = (Template,)


_elements = _Elements()


def start_activity(times: int = 100):
    count = 0
    while count < times:
        count += 1
        logger.info(f"开始第{count}次挑战"), touch(_elements.challenge_tpl)
        # 等待完成
        logger.info("等待奖励刷新"), wait(_elements.reward_tpl, timeout=30)
        logger.info("领取奖励"), touch(_elements.reward_tpl)
