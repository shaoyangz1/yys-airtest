from airtest.core.api import *
from pydantic.main import BaseModel

from settings import settings, logger

_PATH = "static/template/rank"


class _Elements(BaseModel):
    """图像模版"""

    rank_tpl = Template(settings.ROOT.joinpath(_PATH, "rank_icon.png"))
    fight_tpl = Template(settings.ROOT.joinpath(_PATH, "fight_icon.png"))
    fight1_tpl = Template(settings.ROOT.joinpath(_PATH, "fight1_icon.png"))
    prepare_tpl = Template(settings.ROOT.joinpath(_PATH, "prepare_icon.png"))
    team_auto_tpl = Template(settings.ROOT.joinpath(_PATH, "team_auto.png"))
    manual_tpl = Template(settings.ROOT.joinpath(_PATH, "manual_icon.png"))
    complete_tpl = Template(settings.ROOT.joinpath(_PATH, "complete_icon.png"))
    back_tpl = Template(settings.ROOT.joinpath(_PATH, "back_icon.png"))
    confirm_tpl = Template(settings.ROOT.joinpath(_PATH, "confirm_icon.png"))
    reward_tpl = Template(settings.ROOT.joinpath(_PATH, "reward_icon.png"))
    quit_tpl = Template(settings.ROOT.joinpath(_PATH, "quit_icon.png"))

    class Config:
        arbitrary_types_allowed = True
        ignored_types = (Template,)


class RankPage:
    """斗技"""

    _elements = _Elements()

    def start_rank(self, times: int = 10):
        """开启斗技
        :type times: rank次数
        """
        while times > 0:
            if exists(self._elements.fight_tpl):
                logger.info("进行战斗匹配"), click(self._elements.fight_tpl)
            elif exists(self._elements.fight1_tpl):
                logger.info("进行战斗匹配"), click(self._elements.fight1_tpl)
            else:
                logger.error("无法开启战斗")
                return
            try:
                time.sleep(5)  # 动画过渡
                if exists(self._elements.team_auto_tpl):
                    logger.error("自动上阵"), click(self._elements.team_auto_tpl)
                else:
                    wait(self._elements.prepare_tpl, timeout=30)
                    logger.info("准备战斗"), click(self._elements.prepare_tpl)
                time.sleep(10)
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
                time.sleep(5)  # 动画过渡
                if exists(self._elements.reward_tpl):
                    logger.info("奖励领取"), click(self._elements.reward_tpl)
                    click(self._elements.reward_tpl)  # 领取奖励完再点击一下关闭奖励
            times -= 1
