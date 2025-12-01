""""This Module defines the Chequing Account class"""

__author__ = "Keith Robles"
__version__ = "1.0.1"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    Chequing Account Class extends from BankAccount
    """
    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date, overdraft_limit: float,
                 overdraft_rate: float):
        """
        __init___: initializes class members to passed parameters.

        new args:
            overdraft_limit: The maximum amount a balance can be overdrawn (below 0.00)
                            before overdraft fees are applied.
            overdraft_rate: The rate to which overdraft fees will be applied.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Directly Assigns Overdraft Values to Overdraft Strategy
        # Changed from before to reduce code and redundancy
        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

        # Checking is done in strategy and then set as Attributes
        self.__overdraft_limit = self.__strategy._OverdraftStrategy__overdraft_limit
        self.__overdraft_rate = self.__strategy._OverdraftStrategy__overdraft_rate

    def __str__(self) -> str:
        return (f"{super().__str__()} \n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate}% "
                f"Account Type: Chequing")

    def get_service_charges(self) -> float:
        """
        returns:
            float: value is calculated in OverdraftStrategy then returned.
        """
        return self.__strategy.calculate_service_charges(self)
    
    