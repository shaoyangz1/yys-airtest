from pydantic.main import BaseModel
from airtest.core.api import *

from settings import settings, logger


class _Elements(BaseModel):
    """图像模版"""
    activity_tpl = Template(settings.ROOT.joinpath("static/template/main", "activity_icon.png"))
    search_tpl = Template(settings.ROOT.joinpath("static/template/main", "search_icon.png"))

    class Config:
        arbitrary_types_allowed = True


class MainPage:
    """首页"""
    _elements = _Elements()

    def enter_activity(self):
        """进入町中"""
        logger.info("从首页进入町中"), click(self._elements.activity_tpl)

    def start_search(self):
        """进入探索"""
        logger.info("从首页进入探索"), click(self._elements.search_tpl)
