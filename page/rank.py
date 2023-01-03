from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger

_PATH = "static/template/rank"


class _Elements(BaseModel):
    """图像模版"""

    rank_tpl = Template(settings.ROOT.joinpath(_PATH, "rank_icon.png"))
    fight_tpl = Template(settings.ROOT.joinpath(_PATH, "fight_icon.png"))
    fight_protect_tpl = Template(
        settings.ROOT.joinpath(_PATH, "fight_protect_icon.png")
    )
    prepare_tpl = Template(settings.ROOT.joinpath(_PATH, "prepare_icon.png"))
    manual_tpl = Template(settings.ROOT.joinpath(_PATH, "manual_icon.png"))
    complete_tpl = Template(settings.ROOT.joinpath(_PATH, "complete1_icon.png"))
    back_tpl = Template(settings.ROOT.joinpath(_PATH, "back_icon.png"))
    confirm_tpl = Template(settings.ROOT.joinpath(_PATH, "confirm_icon.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward_icon.png"))
    quit_tpl = Template(settings.ROOT.joinpath(_PATH, "quit_icon.png"))

    class Config:
        arbitrary_types_allowed = True


class RankPage:
    """斗技"""

    _elements = _Elements()

    def start_rank(self, times: int = 10):
        """开启斗技
        :type times: rank次数
        """
        if exists(self._elements.rank_tpl):
            logger.info("进入斗技场馆"), click(self._elements.rank_tpl)
        else:
            logger.info("已在斗技场馆")
        while times > 0:
            if exists(self._elements.fight_tpl):
                logger.info("进行战斗匹配"), click(self._elements.fight_tpl)
            elif exists(self._elements.fight_protect_tpl):
                logger.info("进行战斗匹配"), click(self._elements.fight_protect_tpl)
            else:
                logger.error("无法开启战斗")
                return
            try:
                wait(self._elements.prepare_tpl, timeout=30)
                logger.info("准备战斗"), click(self._elements.prepare_tpl)
                time.sleep(10)
                if exists(self._elements.manual_tpl):
                    time.sleep(3)
                    logger.info("切换自动战斗"), click(self._elements.manual_tpl)
                else:
                    logger.info("正在自动战斗")
                count = 60
                while count > 0:
                    #  战斗180s 没结束就投降
                    try:
                        loop_find(self._elements.complete_tpl, timeout=3)
                        logger.info("战斗结束"), click(self._elements.complete_tpl)
                        break
                    except TargetNotFoundError:
                        count -= 1
                else:
                    logger.info("准备投降"), click(self._elements.back_tpl)
                    logger.info("确认投降"), click(self._elements.confirm_tpl)
                    logger.info("战斗完成"), click(self._elements.complete_tpl)
            except TargetNotFoundError:
                #  对方投降触发异常
                if exists(self._elements.complete_tpl):
                    logger.info("战斗结束"), click(self._elements.complete_tpl)
            finally:
                #  检测一下有没有奖励
                if exists(self._elements.reward_tpl):
                    logger.info("奖励领取"), click(self._elements.reward_tpl)
                    click(self._elements.fight_tpl)  # 领取奖励完再点击一下关闭奖励
            times -= 1
        logger.info("离开斗技场馆"), click(self._elements.quit_tpl)
