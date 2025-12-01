"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    
    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

    def test_init_valid(self):
        # Arrange & Act
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

        # Assert
        self.assertEqual(1010, client.client_number)
        self.assertEqual("Susan", client.first_name)
        self.assertEqual("Clark", client.last_name)
        self.assertEqual("susanclark@pixell.com", client.email_address)

    def test_init_invalid_client_number_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client("A", "Susan", "Clark", "susanclark@pixell.com")

    def test_init_invalid_first_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client(1010, " ", "Clark", "susanclark@pixell.com")

    def test_init_invalid_last_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client(1010, "Susan", " ", "susanclark@pixell.com")

    def test_init_invalid_email_set_to_default_email(self):
        # Arrange & Act
        client = Client(1010, "Susan", "Clark", "not a email")
        expected = "email@pixell-river.com"

        # Assert
        self.assertEqual(expected, client.email_address)

    def test_client_number_returns_client_number_attribute(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual(1010, self.client.client_number)

    def test_client_number_returns_first_name_attribute(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual("Susan", self.client.first_name)
    
    def test_client_number_returns_last_name_attribute(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual("Clark", self.client.last_name)
    
    def test_client_number_returns_email_address_attribute(self):
        # Arrange done by setup above...
        # Act and Assert
        self.assertEqual("susanclark@pixell.com", self.client.email_address)

    def test_str(self):
        # Arrange done by setup above...
        expected = "Clark, Susan [1010] - susanclark@pixell.com"

        # Act and Assert
        self.assertEqual(expected, str(self.client))