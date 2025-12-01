"""
Description: Unit tests for the InvestmentAccount class.
Author: Keith Robles
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class TestClient(unittest.TestCase):

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.investment_account  = InvestmentAccount(20025, 1, 0,
                                                     date(2012, 6, 6), 2.00)
        self.BASE_SERVICE_CHARGE = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        
    def test_init_valid(self):
        # Arrange & Act
        investment_account  = InvestmentAccount(20025, 1, 0,
                                                date(2025, 6, 6), 2.00)
        management_fee = investment_account._InvestmentAccount__management_fee

        # Assert
        self.assertEqual(2.00, management_fee)

    def test_init_invalid(self):
        # Arrange & Act
        investment_account  = InvestmentAccount(20025, 1, 0,
                                                date(2025, 6, 6), "Two")
        management_fee = investment_account._InvestmentAccount__management_fee

        # Assert
        self.assertEqual(2.55, management_fee)

    def test_get_service_change_when_date_created_more_than_ten_years_ago(self):
        # Arrange done by setup above...
        service_charge = self.investment_account.get_service_charges()

        # Act & Assert
        self.assertEqual(self.BASE_SERVICE_CHARGE, service_charge)

    def test_get_service_change_when_date_created_exactly_ten_years_ago(self):
        # Arrange & Act
        # This way it'll always be exactly 10 years ago
        ten_years_ago = date.today() - timedelta(days = 10 * 365.25) 

        investment_account  = InvestmentAccount(20025, 1, 0,
                                                ten_years_ago, 2.00)
        service_charge = investment_account.get_service_charges()
        expected = self.BASE_SERVICE_CHARGE + 2.00

        # Assert
        self.assertEqual(expected, service_charge)        

    def test_get_service_change_when_date_created_within_ten_years_ago(self):
        # Arrange & Act
        # This way it'll always be within 10 years ago
        within_ten_years_ago = date.today() - timedelta(days = 9 * 365.25) 

        investment_account  = InvestmentAccount(20025, 1, 0,
                                                within_ten_years_ago, 2.00)
        service_charge = investment_account.get_service_charges()
        expected = self.BASE_SERVICE_CHARGE + 2.00

        # Assert
        self.assertEqual(expected, service_charge)

    def test_str_displays_when_more_than_ten_years_ago(self):
        # Arrange done by setup above...
        expected = ("Account Number: 20025 Balance: $0.00 \n"
                    "Date Created: 2012-06-06 " 
                    "Management Fee: $2.00 "
                    "Account Type: Investment")

        # Act and Assert
        self.assertEqual(expected, str(self.investment_account))

    def test_str_displays_within_ten_years_ago(self):
        # Arrange done by setup above...
        # This way it'll always be within 10 years ago
        within_ten_years_ago = date.today() - timedelta(days = 9 * 365.25)
        investment_account  = InvestmentAccount(20025, 1, 0,
                                                within_ten_years_ago, 2.00)
        expected = ("Account Number: 20025 Balance: $0.00 \n"
                    f"Date Created: {within_ten_years_ago} " 
                    "Management Fee: $2.00 "
                    "Account Type: Investment")

        # Act and Assert
        self.assertEqual(expected, str(investment_account))

    