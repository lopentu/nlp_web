from typing import Any, Union
from .actions import WSGKind, Action


def reducer(state, action: Action) -> Union[str, Any]:
    """The reducer function generates new states."""

    initial_state = (state != None) if state else ""

    if action["kind"] == WSGKind.ADD_WSG:
        return action["payload"]

    return initial_state
