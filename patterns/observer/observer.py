"""This module defines the Observer class."""

__author__ = "Keith Robles"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstract Class for Observing.
    Methods:
        update: Abstract method which will be implemented
            in concrete classes to notify observers when there 
            are changes in the subject.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Abstract method that will be used by concrete classes.
        returns:
            null
        """
        pass