"""This module defines the Subject class."""

__author__ = "Keith Robles"
__version__ = "1.0.0"

from patterns.observer.observer import Observer

class Subject(Observer):
    """
    Subject Observer Class
    Methods:
        attach: Method for attaching the observer
        detach: Method for detaching the observer
        notify: Method for giving an update via message
    """
    def __init__(self) -> None:
        self._observers = []

    def attach(self, observer: Observer) -> None:
        pass

    def detach(self, observer: Observer) -> None:
        pass

    def notify(self, message: str) -> None:
        pass

    def update(self, message: str) -> None:
        pass