from io import BufferedWriter
from ..spiders import PttSpider
from typing import Any, Dict, Tuple
from scrapy.exporters import BaseItemExporter, CsvItemExporter


class CsvPipeline:
    """
    The CsvPipeline object writes the scraped item to csv.
    """

    def open_spider(self, spider: PttSpider):
        self.exporters_list: Dict[str, Tuple[BaseItemExporter, BufferedWriter]] = {}

    def _exporter_for_item(self, item: Dict[str, Any]) -> CsvItemExporter:
        board = item.pop("board")

        if board not in self.exporters_list:
            file = open(f"{board}.csv", "wb")
            exporter = CsvItemExporter(file)
            exporter.start_exporting()
            self.exporters_list[board] = (exporter, file)

        return self.exporters_list[board][0]

    def process_item(self, item: Dict[str, Any], spider: PttSpider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item

    def close_spider(self, spider: PttSpider):
        for exporter, csv_file in self.exporters_list.values():
            exporter.finish_exporting()
            csv_file.close()
