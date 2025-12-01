""""This Module defines the Savings Account class"""

__author__ = "Keith Robles"
__version__ = "1.0.1"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    Savings Account Class extends from BankAccount
    """

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date,
                 minimum_balance: float):
        """
        __init___: initializes class members to passed parameters.

        new args:
            minimum_balance (float): a float which stores a minimum value a balance
                                    can be before further service charges are applied
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Directly Assigns Overdraft Values to Overdraft Strategy
        # Changed from before to reduce code and redundancy
        self.__strategy = MinimumBalanceStrategy(minimum_balance)

        # Checking is done in strategy and then set as Attributes
        self.__minimum_balance = self.__strategy._MinimumBalanceStrategy__minimum_balance

    def __str__(self) -> str:
        return (f"{super().__str__()} \n"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} "
                f"Account Type: Savings")

    def get_service_charges(self) -> float:
        """
        returns:
            float: value is calculated in MinimumBalanceStrategy then returned.
        """
        return self.__strategy.calculate_service_charges(self)