from pathlib import Path
from typing import Any, Dict
from datetime import datetime
from .base import BasePipeline
from ..spiders import PttSpider
from scrapy.exporters import JsonItemExporter


class JsonPipeline(BasePipeline):
    """
    The JsonPipeline object writes the scraped item to json.
    """

    def _exporter_for_item(self, item: Dict[str, Any], spider: PttSpider):
        data_dir = spider.data_dir
        board = item["board"]
        timestamp = int(
            datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S").strftime("%s")
        )
        date = datetime.fromtimestamp(timestamp)
        formatted_date = date.strftime("%Y%m%d_%H%M")
        year = date.year
        dir_path = f"{data_dir}/{board}/{year}"
        file_path = f"{dir_path}/{formatted_date}_{item['post_id']}"
        Path(dir_path).mkdir(parents=True, exist_ok=True)

        if file_path not in self.exporters_list:
            file = open(f"{file_path}.json", "wb")
            exporter = JsonItemExporter(file, encoding="utf-8")
            exporter.start_exporting()
            self.exporters_list[file_path] = (exporter, file)

        return self.exporters_list[file_path][0]

    def process_item(self, item: Dict[str, Any], spider: PttSpider) -> Dict[str, Any]:
        exporter = self._exporter_for_item(item, spider)
        exporter.export_item(item)
        return item
