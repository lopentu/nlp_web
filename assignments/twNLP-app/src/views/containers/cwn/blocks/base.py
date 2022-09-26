from abc import ABC, abstractmethod


class Block(ABC):
    """
    The Block object defines the behaviour for creating a display block.
    """

    @abstractmethod
    def visualize(self):
        """The visualize method visualizes the streamlit component."""
        pass
