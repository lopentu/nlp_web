from .reducer import reducer
from utils.stores import Store
from typing import Callable, List, Union

wsg_store = None


def return_value():
    return wsg_store.get_state()


wsg_store = Store(reducer)

wsg_store.add_listener(return_value)


def use_WSG() -> List[Union[str, Callable]]:
    """The use_WSG function contains wsg result and and wsg dispatcher."""
    return [wsg_store.get_state(), wsg_store.dispatch]
