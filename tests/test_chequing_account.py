"""
Description: Unit tests for the ChequingAccount class.
Author: Keith Robles
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestClient(unittest.TestCase):
    
    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.chequing_account = ChequingAccount(20025, 1, 0, 
                                                date(2025, 6, 6), -100, 0.05)
        
    def test_init_valid(self):
        # Arrange & Act
        chequing_account = ChequingAccount(20025, 1, 0, 
                                           date(2025, 6, 6), -100, 0.05)
        overdraft_limit = chequing_account._ChequingAccount__overdraft_limit
        overdraft_rate = chequing_account._ChequingAccount__overdraft_rate

        # Assert
        self.assertEqual(date(2025, 6, 6), chequing_account._date_created)
        self.assertEqual(-100, overdraft_limit)
        self.assertEqual(0.05, overdraft_rate)

    def test_init_overdraft_limit_invalid_type(self):
        # Arrange & Act
        chequing_account = ChequingAccount(20025, 1, 0, 
                                           date(2025, 6, 6), "Nothing", 0.05)
        overdraft_limit = chequing_account._ChequingAccount__overdraft_limit

        # Assert
        self.assertEqual(-100, overdraft_limit)

    def test_init_overdraft_rate_invalid_type(self):
        # Arrange & Act
        chequing_account = ChequingAccount(20025, 1, 0, 
                                           date(2025, 6, 6), -100, "Nothing")
        overdraft_rate = chequing_account._ChequingAccount__overdraft_rate

        # Assert
        self.assertEqual(0.05, overdraft_rate)

    def test_init_date_created_invalid_type(self):
        # Arrange & Act
        chequing_account = ChequingAccount(20025, 1, 0, 
                                           "June 6, 2025", -100, 0.05)

        # Assert
        self.assertEqual(date.today(), chequing_account._date_created)

    def test_service_charges_when_balance_greater_than_overdraft_limit(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual(0.5, 
                        round(self.chequing_account.get_service_charges(), 2))

    def test_service_charges_when_balance_less_than_overdraft_limit(self):
        # Arrange & Act
        chequing_account = ChequingAccount(20025, 1, -600, 
                                           date(2025, 6, 6), -100, 0.05)

        # Act and Assert
        self.assertEqual(25.5, 
                        round(chequing_account.get_service_charges(), 2))

    
    def test_service_charges_when_balance_equal_to_overdraft_limit(self):
        # Arrange & Act
        chequing_account = ChequingAccount(20025, 1, -100, 
                                           date(2025, 6, 6), -100, 0.05)

        # Act and Assert
        self.assertEqual(0.5, 
                        round(chequing_account.get_service_charges(), 2))
        
    def test_str(self):
        # Arrange done by setup above...
        expected = ("Account Number: 20025 Balance: $0.00 \n" 
                    "Overdraft Limit: $-100.00 "
                    "Overdraft Rate: 0.05% "
                    "Account Type: Chequing")

        # Act and Assert
        self.assertEqual(expected, str(self.chequing_account))