import json
from pathlib import Path
from typing import Any, Dict
from datetime import datetime
from ..spiders import PttSpider


class JsonPipeline:
    """
    The JsonPipeline object writes the scraped item to json.
    """

    def process_item(self, item: Dict[str, Any], spider: PttSpider) -> None:
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

        with open(f"{file_path}.json", "w", encoding="utf-8") as file:
            json.dump(item, file, ensure_ascii=False)

        return item
