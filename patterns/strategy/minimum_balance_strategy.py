"""This module defines the Overdraft Strategy class."""

__author__ = "Keith Robles"
__version__ = "1.0.0"

from bank_account import *
from bank_account.bank_account import BankAccount # Python doesn't like this being in __all__ 
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Minimum Balance Strategy Class
    Methods:
        calculate_service_charges: Method which extends the
            calculate_service_charges Method of the ServiceChargeStrategy 
            Abstract class
    """
     # Constant for Premium Charge
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        __init___: initializes class members to passed parameters.

        args:
            overdraft_limit: The maximum amount a balance can be overdrawn (below 0.00)
                            before overdraft fees are applied.
            overdraft_rate: The rate to which overdraft fees will be applied.
        """
        if isinstance(minimum_balance, (float, int)):
            self.__minimum_balance = float(minimum_balance)
        else:
            self.__minimum_balance = 50.00

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        calculate_service_charges method
        returns:
            float
        """
        balance = account.balance

        if (balance >= self.__minimum_balance):
            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE *
                            self.SERVICE_CHARGE_PREMIUM)
        return service_charge