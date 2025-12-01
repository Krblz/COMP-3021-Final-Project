"""
Description: Unit tests for the SavingsAccount class.
Author: Keith Robles
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestClient(unittest.TestCase):

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.savings_account  = SavingsAccount(20025, 1, 500,
                                                     date(2012, 6, 6), 50)
        
    def test_init_valid(self):
        # Arrange & Act
        savings_account  = SavingsAccount(20025, 1, 0,
                                                date(2025, 6, 6), 50)
        min_balance = savings_account._SavingsAccount__minimum_balance

        # Assert
        self.assertEqual(50.00, round(min_balance, 2))

    def test_init_invalid(self):
        # Arrange & Act
        savings_account  = SavingsAccount(20025, 1, 0,
                                                date(2025, 6, 6), "Fifty")
        min_balance = savings_account._SavingsAccount__minimum_balance

        # Assert
        self.assertEqual(50.00, round(min_balance, 2))

    def test_get_service_charges_when_balance_greater_than_minimum(self):
        # Arrange & Act
        savings_account  = SavingsAccount(20025, 1, 500,
                                                date(2025, 6, 6), 50)
        min_balance = savings_account.get_service_charges()

        # Assert
        self.assertEqual(0.5, round(min_balance, 2))

    def test_get_service_charges_when_balance_equal_to_minimum(self):\
        # Arrange & Act
        savings_account  = SavingsAccount(20025, 1, 50,
                                                date(2025, 6, 6), 50)
        min_balance = savings_account.get_service_charges()

        # Assert
        self.assertEqual(0.5, round(min_balance, 2))
    
    def test_get_service_charges_when_balance_less_than_minimum(self):
        # Arrange & Act
        savings_account  = SavingsAccount(20025, 1, 25,
                                                date(2025, 6, 6), 50)
        min_balance = savings_account.get_service_charges()

        # Assert
        self.assertEqual(1, round(min_balance, 2))

    def test_str(self):
        # Arrange done by setup above...
        # This way it'll always be within 10 years ago
        expected = ("Account Number: 20025 Balance: $500.00 \n"
                    f"Minimum Balance: $50.00 "
                    f"Account Type: Savings")

        # Act and Assert
        self.assertEqual(expected, str(self.savings_account))