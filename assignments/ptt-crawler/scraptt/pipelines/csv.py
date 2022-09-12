from pathlib import Path
from io import BufferedWriter
from datetime import datetime
from ..spiders import PttSpider
from typing import Any, Dict, Tuple
from scrapy.exporters import BaseItemExporter, CsvItemExporter


class CsvPipeline:
    """
    The CsvPipeline object writes the scraped item to csv.
    """

    def open_spider(self, spider: PttSpider) -> None:
        self.exporters_list: Dict[str, Tuple[BaseItemExporter, BufferedWriter]] = {}

    def _exporter_for_item(
        self, item: Dict[str, Any], spider: PttSpider
    ) -> CsvItemExporter:
        data_dir = spider.data_dir
        board = item.pop("board")
        date = datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S")
        year = date.year
        month = date.month
        dir_path = f"{data_dir}/{board}/{year}"
        file_path = f"{dir_path}/{board}_{year}_{month}"
        Path(dir_path).mkdir(parents=True, exist_ok=True)

        if file_path not in self.exporters_list:
            file = open(f"{file_path}.csv", "wb")
            exporter = CsvItemExporter(file)
            exporter.start_exporting()
            self.exporters_list[file_path] = (exporter, file)

        return self.exporters_list[file_path][0]

    def process_item(self, item: Dict[str, Any], spider: PttSpider) -> Dict[str, Any]:
        exporter = self._exporter_for_item(item, spider)
        exporter.export_item(item)
        return item

    def close_spider(self, spider: PttSpider) -> None:
        for exporter, csv_file in self.exporters_list.values():
            exporter.finish_exporting()
            csv_file.close()
