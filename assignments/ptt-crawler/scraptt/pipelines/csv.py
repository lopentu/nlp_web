from pathlib import Path
from .utils import get_items
from typing import Any, Dict
from datetime import datetime
from .base import BasePipeline
from ..spiders import PttSpider
from scrapy.exporters import CsvItemExporter


class CsvPipeline(BasePipeline):
    """
    The CsvPipeline object writes the scraped item to csv.
    """

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
        csv_item = get_items(
            item,
            [
                "board",
                "author",
                "alias",
                "title",
                "date",
                "ip",
                "city",
                "country",
                "url",
                "post_vote",
            ],
        )

        exporter = self._exporter_for_item(csv_item, spider)
        exporter.export_item(csv_item)
        return csv_item
