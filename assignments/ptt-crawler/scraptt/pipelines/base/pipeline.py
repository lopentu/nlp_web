from io import BufferedWriter
from ...spiders import PttSpider
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple
from scrapy.exporters import BaseItemExporter


class BasePipeline(ABC):
    """
    The BasePipeline object writes the scraped item to different file types.
    """

    def open_spider(self, spider: PttSpider) -> None:
        self.exporters_list: Dict[str, Tuple[BaseItemExporter, BufferedWriter]] = {}

    @abstractmethod
    def _exporter_for_item(self, item: Dict[str, Any], spider: PttSpider):
        pass

    @abstractmethod
    def _exporter_for_item(self, item: Dict[str, Any], spider: PttSpider):
        pass

    def close_spider(self, spider: PttSpider) -> None:
        for exporter, file in self.exporters_list.values():
            exporter.finish_exporting()
            file.close()
