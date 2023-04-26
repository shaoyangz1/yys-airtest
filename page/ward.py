import itertools

from airtest.core.api import *
from page.battle import BattlePage
from pydantic.main import BaseModel

from settings import settings, logger

_PATH = "static/template/ward"


class _Elements(BaseModel):
    """图像模版"""

    ward_tpl = Template(settings.ROOT.joinpath(_PATH, "ward_icon.png"))
    attack_tpl = Template(settings.ROOT.joinpath(_PATH, "attack_icon.png"))

    class Config:
        arbitrary_types_allowed = True


class WardPage:
    def __init__(self):
        self._elements = _Elements()
        self.battle = BattlePage()
        self.ward_list = [
            i for i in itertools.product([400, 800, 1200], [300, 450, 600])
        ]

    def enter_ward(self):
        """进入结界"""
        logger.info("进入结界突破"), touch(self._elements.ward_tpl)

    def start_attack(self):
        ...

    def surrender_wards(self, nums: int = 9):
        """
        结界投降
        :param nums: 投降个数
        """
        for ward in self.ward_list[:nums]:
            logger.info(f"选择结界{ward}"), click(ward)
            logger.info("结界进攻"), click(self._elements.attack_tpl)
            time.sleep(3)  # 动画过度
            logger.info("点击投降"), self.battle.quit_battle()
            time.sleep(2)  # 动画过度
