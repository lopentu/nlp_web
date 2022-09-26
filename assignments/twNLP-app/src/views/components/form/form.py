from typing import Union
from .form_components import add_text_area, add_selectbox, add_multiselect


def form_controller(control: str, **kwargs) -> Union[str, int]:
    """The form_controller function builds a form component based on `control`."""
    form_factories = {
        "text-area": add_text_area,
        "select-box": add_selectbox,
        "multi-select": add_multiselect,
    }

    return form_factories[control](**kwargs)
