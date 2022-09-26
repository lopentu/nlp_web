from typing import Any
from enum import Enum, auto
from types import SimpleNamespace
from dataclasses import dataclass, FrozenInstanceError


class WSGKind(Enum):
    ADD_WSG = auto()
    RESET = auto()


class FrozenSimpleNamespace(SimpleNamespace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, name: str, value: Any) -> None:
        raise FrozenInstanceError(f"cannot assign to field '{name}'")


@dataclass(frozen=True)
class Action:
    """
    The Action object contains the payload of information.
    """

    kind: WSGKind
    payload: dict

    def __post_init__(self):
        super().__setattr__("payload", FrozenSimpleNamespace(**self.payload))
