""""This Module defines the Client class"""

__author__ = "Keith Robles"
__version__ = "1.0.1"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import date, datetime

class Client(Observer):
    """
    Client Class, represents the Client and inherits from the Observer Class
    """
    def __init__(self, client_number: int, first_name: str, last_name: str,
                 email_address: str):
        """
        Initialize the Client Object based on received arguments

        args:
            client_number (int): An integer value representing the client number.
            first_name (str): A string value the client's first name
            last_name (str): A string value the client's last name.
            email_address (str): A string value the client's email address.

        raises:
            ValueError: If any of the arguments are invalid.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric")

        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First Name cannot be blank")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last Name cannot be blank")
        
        try:
            valid = validate_email(email_address, check_deliverability = False)
            self.__email_address = valid.email

        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Accessor for the client_number attribute.
        Returns: int - A number to uniquely identify the Client
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for the first_name attribute.
        Returns: str - The First Name of the Client
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor for the last_name attribute.
        Returns: str - The Last Name of the Client
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Accessor for the email_address attribute.
        Returns: str - The Email address of the Client
        """
        return self.__email_address
    
    def __str__(self) -> str:
        """
        Returns a String Representation of the Client Instance
        Returns: str - The Client Instance as a formatted string.
        """
        return (f"{self.__last_name}, {self.__first_name}"
                f" [{self.__client_number}] - {self.__email_address}")
    
    def update(self, message: str) -> None:
        subject = f"ALERT: Unusual Activity: {date.today()}/{datetime.now()}"
        message = (f"Notification for {self.__client_number}: "
                   f"{self.__first_name} {self.__last_name}: "
                   f"{message}")
        simulate_send_email(self.__email_address, subject, message)