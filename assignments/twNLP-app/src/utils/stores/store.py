from dataclasses import dataclass
from typing import Any, Callable, Dict


@dataclass
class Store:
    """
    The Store object keeps tracks of changes and generates new states via a reducer.
    """

    reducer: Callable

    def __post_init__(self):
        if callable(self.reducer) != True:
            raise ValueError("Expecting a callable reducer function")

        self.__states = None
        self.__listeners = list()
        self.__reducer = self.reducer

    def dispatch(self, action: Dict[str, Any]):
        if type(action) != dict:
            raise ValueError("Expecting action to be of type dictionary")

        has_kind = "kind" in action

        if not has_kind:
            raise ValueError("Action is expected to have an attribute 'kind'")

        currentStates = None

        if type(self.__states) == dict:
            currentStates = self.__states.copy()

        self.__states = self.__reducer(currentStates, action)
        self.__emitListeners()
        pass

    def __emitListeners(self):
        for listener in self.__listeners:
            listener()

    def add_listener(self, callback):
        if callable(callback):
            self.__listeners.append(callback)

    def get_state(self):
        return self.__states
