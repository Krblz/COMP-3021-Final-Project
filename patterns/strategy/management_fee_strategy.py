"""This module defines the Management Fee Strategy class."""

__author__ = "Keith Robles"
__version__ = "1.0.0"

from bank_account import *
from bank_account.bank_account import BankAccount # Python doesn't like this being in __all__ 
from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Management Fee Strategy Class
    Methods:
        calculate_service_charges: Method which extends the
            calculate_service_charges Method of the ServiceChargeStrategy 
            Abstract class
    """
    # Constant for the date 10 years ago
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        __init___: initializes class members to passed parameters.

        new args:
            management_fee (float): a float which stores a flat-rate fee the bank charges
                                    for managing an Investment Account        
        """

        if isinstance(management_fee, (float, int)):
            self.__management_fee = float(management_fee)
        else:
            self.__management_fee = 2.55

        if isinstance(date_created, (date)):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        calculate_service_charges method
        returns:
            float
        """
        if (self.__date_created < self.TEN_YEARS_AGO):
            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE +
                            self.__management_fee)
        return service_charge