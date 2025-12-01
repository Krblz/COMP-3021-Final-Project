"""This module defines the Service Charge Strategy class."""

__author__ = "Keith Robles"
__version__ = "1.0.0"

from bank_account import *
from bank_account.bank_account import BankAccount # Python doesn't like this being in __all__ 
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract Class for Payment Strategies.
    Methods:
        calculate_service_charges: Abstract method which will be implemented
            in each of the subclasses of ServiceChargeStrategy based on the specific
            strategy being employed.
    """

    # Constant for Base Service Charge
    BASE_SERVICE_CHARGE = 0.5

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract calculate_service_charges accessor
        returns:
            float
        """
        pass