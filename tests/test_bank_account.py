"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from datetime import date
from bank_account.bank_account import BankAccount

class TestClient(unittest.TestCase):    
    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.bank_account = MockAccount(20025, 1, 1000, date(2025, 6, 6))

    def test_init_valid(self):
        # Arrange & Act
        bank_account = MockAccount(20025, 1, 1000, date(2025, 6, 6))

        # Assert (uses name mangling to obtain private attribute)
        self.assertEqual(20025, bank_account.account_number)
        self.assertEqual(1, bank_account.client_number)
        self.assertEqual(1000, bank_account.balance)

    def test_init_balance_set_to_0_when_non_numeric(self):
        # Arrange & Act
        bank_account = MockAccount(20025, 1, "1 million", date(2025, 6, 6))
        expected = 0

        # Assert
        self.assertEqual(expected, round(bank_account.balance, 2))

    def test_init_raises_ValueError_when_non_numeric_account_number(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            bank_account = MockAccount("Ten Hundred", 1, 1000, date(2025, 6, 6))

    def test_init_raises_ValueError_when_non_numeric_client_number(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            bank_account = MockAccount(20025, "A01", 1000, date(2025, 6, 6))

    def test_account_number_returns_account_attribute(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual(20025, self.bank_account.account_number)

    def test_account_number_returns_client_number_attribute(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual(1, self.bank_account.client_number)

    def test_account_number_returns_balance_attribute(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual(1000, round(self.bank_account.balance, 2))

    def test_update_balance_correctly_updates_when_amount_is_positive(self):
        # Arrange done partially by setup above...
        amount = 1025
        expected = 2025 # Balance + Amount
        # Act
        self.bank_account.update_balance(amount)

        # Assert
        self.assertEqual(expected, round(self.bank_account.balance, 2))

    def test_update_balance_correctly_updates_when_amount_is_negative(self):
        # Arrange done partially by setup above...
        amount = -100
        expected = 900 # Balance - Amount
        # Act
        self.bank_account.update_balance(amount)

        # Assert
        self.assertEqual(expected, round(self.bank_account.balance, 2))

    def test_update_balance_unchanged_when_amount_is_non_numeric(self):
        # Arrange done partially by setup above...
        amount = "10 Cents"
        expected = 1000
        # Act
        self.bank_account.update_balance(amount)

        # Assert
        self.assertEqual(expected, round(self.bank_account.balance, 2))

    def test_deposit_correctly_updates_when_valid(self):
        # Arrange done partially by setup above...
        amount = 1025
        expected = 2025 # Balance + Amount
        # Act
        self.bank_account.deposit(amount)

        # Assert
        self.assertEqual(expected, round(self.bank_account.balance, 2))

    def test_deposit_raises_ValueError_when_amount_is_negative(self):
        # Arrange done partially by setup above...
        # Arrange & Act
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-500)

    def test_withdraw_correctly_updates_when_valid(self):
        # Arrange done partially by setup above...
        amount = 500
        expected = 500 # Balance - Amount
        # Act
        self.bank_account.withdraw(amount)

        # Assert
        self.assertEqual(expected, round(self.bank_account.balance, 2))

    def test_withdraw_raises_ValueError_when_amount_is_negative(self):
        # Arrange done partially by setup above...
        # Arrange & Act
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-500)

    def test_withdraw_raises_ValueError_when_amount_exceeds_balance(self):
        # Arrange done partially by setup above...
        # Arrange & Act
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-2000) # Setup Balance is 1000

    def test_str(self):
        # Arrange done by setup above...
        expected = "Account Number: 20025 Balance: $1,000.00"

        # Act and Assert
        self.assertEqual(expected, str(self.bank_account))


# Mock Account for Unit Testing, Completely independent of other Subclasses
# Allows for Testing without instantiating or using other Subclasses 
class MockAccount(BankAccount):
    def get_service_charges(self):
        return 0.5