"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

__author__ = "COMP-1327 Faculty"
__version__ = "1.0.2025"

import unittest
from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS
from src.chatbot import get_account_number, get_amount, get_balance, make_deposit, get_task

class TestChatBot(unittest.TestCase):
    # Unit Testing for Account Number Validation
    # Tests for when Account Number entered is not a Number
    def test_get_account_number_returns_TypeError(self):
        #Arrange
        user_input = "NotNumbers"
        expected = "Account number must be an int type."        

        #Act and Assert
        with patch('builtins.input', return_value=user_input):            
            with self.assertRaises(TypeError) as context:
                get_account_number()

        self.assertEqual(str(context.exception), expected)    
            
    # Tests for when Account Number entered is not a Valid Number
    def test_get_account_number_returns_ValueError(self):
        #Arrange
        user_input = "112233"
        expected = "Account number entered does not exist."

        #Act and Assert
        with patch('builtins.input', return_value=user_input):            
            with self.assertRaises(ValueError) as context:
                get_account_number()
  
        self.assertEqual(str(context.exception), expected)    

    # Tests for when Account Number entered is a Valid Number
    def test_get_account_number_returns_Valid_Account_Number(self):
        #Arrange
        user_input = "123456"
        expected = 123456

        #Act
        with patch('builtins.input', return_value=user_input):
            actual = get_account_number()

        #Assert        
        self.assertEqual(expected, actual)

    # Unit Testing for get_amount() Function
    # Tests for when amount entered is Non-Numeric
    def test_get_amount_entered_not_numeric(self):
        #Arrange
        user_input = "NotNumbers"
        expected = "Amount must be a numeric type."

        #Act
        with patch('builtins.input', return_value=user_input):            
            with self.assertRaises(TypeError) as context:
                get_amount()

        #Assert
        self.assertEqual(str(context.exception), expected)

    # Tests for when amount entered is equal to 0
    def test_get_amount_equal_zero(self):
        #Arrange
        user_input = "0"
        expected = "Amount must be a value greater than zero."

        #Act and Assert
        with patch('builtins.input', return_value=user_input):            
            with self.assertRaises(ValueError) as context:
                get_amount()

        self.assertEqual(str(context.exception), expected)

    # Tests for when amount entered is less than 0
    def test_get_amount_less_than_zero(self):
        #Arrange
        user_input = "-10"
        expected = "Amount must be a value greater than zero."

        #Act and Assert
        with patch('builtins.input', return_value=user_input):            
            with self.assertRaises(ValueError) as context:
                get_amount()

        self.assertEqual(str(context.exception), expected)                    

    def test_get_valid_amount(self):        
        #Arrange
        user_input = "100"
        expected = 100

        #Act
        with patch('builtins.input', return_value=user_input):
            actual = get_amount()

        #Assert        
        self.assertEqual(expected, actual)
    
    # Unit Testing for get_balance() Function
    # Tests for when the parameter value is not an integer type.
    def test_get_balance_parameter_value_not_integer(self):
        #Arrange
        parameter_value = "NotNumbers"
        expected = "Account number must be an int type."        

        #Act and Assert                
        with self.assertRaises(TypeError) as context:
            get_balance(parameter_value)

        self.assertEqual(str(context.exception), expected)

    # Tests for when the parameter value doest not exist in ACCOUNTS dictionary
    def test_get_balance_parameter_value_not_in_ACCOUNTS(self):
        #Arrange
        parameter_value = "111333"
        expected = "Account number entered does not exist."        

        #Act and Assert       
        with self.assertRaises(ValueError) as context:
            get_balance(parameter_value)

        self.assertEqual(str(context.exception), expected)
    
    # Tests for when function returns a string containing the expected message
    def test_get_balance_returns_expected_message(self):        
        #Arrange
        parameter_value = "123456"
        account_number = int(parameter_value)
        account_balance = ACCOUNTS[account_number]["balance"]
        expected = f"Your current balance for account {account_number} is ${account_balance:,.2f}."

        #Act
        actual = get_balance(parameter_value)
        
        #Assert        
        self.assertEqual(expected, actual)

    # Unit Testing for make_deposit() Function
    # Tests for when the parameter value is not an integer type.
    def test_make_deposit_parameter_value_not_integer(self):
        #Arrange
        #Account_number is the Parameter Values
        account_number = "NotNumber"
        #Amount can be anything
        amount = 42344
        expected = "Account number must be an int type."        

        #Act and Assert                
        with self.assertRaises(TypeError) as context:
            make_deposit(account_number, amount)

        self.assertEqual(str(context.exception), expected)

    # Tests for when the parameter value does not exist in the ACCOUNTS dictionary
    def test_make_deposit_parameter_value_not_in_accounts(self):
        #Arrange
        #Account_number is the Parameter Values
        account_number = "135322"
        #Amount can be anything
        amount ="NotNumbers"
        expected = "Account number must be an int type."        

        #Act and Assert                
        with self.assertRaises(TypeError) as context:
            make_deposit(account_number, amount)

        self.assertEqual(str(context.exception), expected)
    
    # Tests for when the amount entered is not numeric
    def test_make_deposit_amounted_entered_not_numeric(self):
        #Arrange
        #Account_number is the Parameter Values
        account_number = 123456
        amount ="NotNumbers"
        expected = "Amount must be a numeric type."        

        #Act and Assert     
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, amount)

        self.assertEqual(str(context.exception), expected)
    
    # Tests for when the amount entered is equal to zero
    def test_make_deposit_amounted_entered_not_equal_zero(self):
        #Arrange
        #Account_number is the Parameter Values
        account_number = 123456
        amount = 0
        expected = "Amount must be a value greater than zero."  

        #Act and Assert            
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, amount)

        self.assertEqual(str(context.exception), expected)

    # Tests for when the amount entered is less than zero
    def test_make_deposit_amounted_entered_less_than_zero(self):
        #Arrange
        #Account_number is the Parameter Values
        account_number = 123456
        amount = -1
        expected = "Amount must be a value greater than zero."        

        #Act and Assert            
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, amount)

        self.assertEqual(str(context.exception), expected)

    # Tests for when the function returns containing the expected message
    def test_make_deposit_amounted_entered_is_Valid(self):
        #Arrange
        #Account_number is the Parameter Values
        account_number = 123456
        amount = 1000
        expected = f"You have made a deposit of ${amount:,.2f} to account {account_number}."    

        #Act      
        actual = make_deposit(account_number, amount)

        #Assert
        self.assertEqual(actual, expected)
    
    # Test for when an exception is raised when an invalid task is entered
    def test_get_task_invalid_task_entered(self):
        #Arrange
        user_input = "withdraw"
        expected = '"withdraw" is an unknown task.'  

        #Act and Assert            
        with patch('builtins.input', return_value=user_input):            
            with self.assertRaises(ValueError) as context:
                get_task()

        self.assertEqual(str(context.exception), expected)
    
    # Tests for when a valid task is entered and is in lowercase characters
    def test_get_task_valid_and_lowercase(self):
        #Arrange
        user_input = "DEPOSIT"
        expected = "deposit"

        #Act     
        with patch('builtins.input', return_value=user_input):            
            actual = get_task()

        #Assert
        self.assertEqual(expected, actual)
    