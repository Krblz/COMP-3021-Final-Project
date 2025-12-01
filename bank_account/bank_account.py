""""This Module defines the Bank Account class"""

__author__ = "Keith Robles"
__version__ = "1.1.2"

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
    """
    Bank Account Class, represents the Client's Bank Account  
      
    constants:
        LARGE_TRANSACTION_THRESHOLD (float): determines the maximum transaction 
        LOW_BALANCE_LEVEL (float):  determines the low balance level
    """
    LARGE_TRANSACTION_THRESHOLD = 9999.99 
    LOW_BALANCE_LEVEL = 50.0 

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date):
        """
        Initializes a Bank Account object based on received arguments (if valid)
        
        args: 
            account_number (int): An integer value representing the bank account number.
            client_number (int): An integer value representing the client number 
                                representing the account holder.
            balance (float): A float value representing the current balance of the bank account.
            date_created (date): A date value representing the date of bank account creation
        
        raises:
            ValueError: If any of the arguments are invalid.
        """
        super().__init__()

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be numeric")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric")
    
        if isinstance(balance, (float, int)):
            self.__balance = float(balance)
        else:
            self.__balance = 0

        if isinstance(date_created, (date)):
            self._date_created = date_created
        else:
            self._date_created = date.today()


    @property
    def account_number(self) -> int:
        """
        Accessor for the account number attribute.
        Returns: int - The account number of the Bank Account instance
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.
        Returns: int - The client number of the Bank Account instance
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for the balance number attribute.
        Returns: float - The balance of the Bank Account instance
        """
        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """
        Update Balance Method for updating the balance attribute.
        The amount received can be a negative value which, when added to the
        balance, will reduce the balance.
        Depending on the balance of the instance, and the incoming amount
        value, this method could result in a negative balance

        args:
            amount (float): A float value representing the amount 
                            to be added/subtracted to the balance attribute
        """
        if isinstance(amount, (float, int)):
            self.__balance += float(amount)
        
        if self.__balance < self.LOW_BALANCE_LEVEL:
            message = (f"Low balance warning ${self.__balance:,.2f}: "
                       f"on account {self.__account_number}")
            self.notify(message)
        
        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            message = (f"Large transaction ${amount:,.2f}: "
                       f"on account {self.__account_number}")
            self.notify(message)

    def deposit(self, amount: float) -> None:
        """
        Deposit Method for depositing amount to balance.
        The amount received is checked if it is valid.
        If it is valid, balance will be updated
        If it is invalid, an error will be raised.

        args:
            amount (float): A float value representing the amount
                            to be validated.
        
        raises:
            ValueError: If any of the arguments are invalid.
        """
        if not isinstance(amount, (float, int)):
            raise ValueError(f"Deposit amount: {amount} must be numeric")
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount} must be positive")            
        self.update_balance(amount)         

    def withdraw(self, amount: float) -> None:
        """
        Withdraw Method for withdrawing amount from balance.
        The amount received is checked if it is valid.
        If it is valid, balance will be updated
        If it is invalid, an error will be raised.
        """
        if not isinstance(amount, (float, int)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric")
        if amount <= 0:
            raise ValueError(f"Withdraw amount: {amount} must be positive")
        if amount > self.__balance:
            raise ValueError(f"Withdraw amount: {amount} must not "
                             f"exceed the account balance: {self.__balance}.")        
        # Amount is multiplied by negative 1 to reduce Balance         
        self.update_balance(amount * -1)    

    def __str__(self) -> str:
        """
        Returns a string representation of the Bank Account instance.
        Returns: str - The Bank Account instance as a formatted string.
        """
        return (f"Account Number: {self.__account_number} "
                f"Balance: ${self.__balance:,.2f}")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        pass

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)
    
