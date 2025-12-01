""""This Module defines the Investment Account class"""

__author__ = "Keith Robles"
__version__ = "1.0.1"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    Investment Account Class extends from BankAccount
    """

    # Constant for the date 10 years ago
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date,
                 management_fee: float):
        """
        __init___: initializes class members to passed parameters.

        new args:
            management_fee (float): a float which stores a flat-rate fee the bank charges
                                    for managing an Investment Account        
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Directly Assigns Overdraft Values to Overdraft Strategy
        # Changed from before to reduce code and redundancy
        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

        # Checking is done in strategy and then set as Attributes
        self.__management_fee = self.__strategy._ManagementFeeStrategy__management_fee

    def __str__(self) -> str:
        return (f"{super().__str__()} \n"
                f"Date Created: {self._date_created} "
                f"Management Fee: ${self.__management_fee:,.2f} "
                f"Account Type: Investment")

    def get_service_charges(self) -> float:      
        """
        returns:
            float: value is calculated in ManagementFeeStrategy then returned.
        """
        return self.__strategy.calculate_service_charges(self)