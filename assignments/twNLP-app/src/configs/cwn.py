from pathlib import Path
from typing import Optional


cwn_model_path = Path.home().resolve() / ".cwn_graph"


def download_cwn_models(upgrade: Optional[bool] = False):
    import CwnSenseTagger, DistilTag
    from CwnGraph import CwnImage

    DistilTag.download(upgrade=upgrade)
    CwnSenseTagger.download(upgrade=upgrade)
    CwnImage.latest()
