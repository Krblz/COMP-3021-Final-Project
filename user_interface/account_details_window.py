__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Keith Robles"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """

    # Signal for Balance Update
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        if isinstance(account, BankAccount):
            self.__account = copy.copy(account)
            self.account_number_label.setText(str(self.__account.account_number))
            self.balance_label.setText(str(self.__account.balance))

            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.close()

    @Slot()
    def __on_apply_transaction(self):
        try: # Attempts to converts Transaction Amount Edit to Float
            transaction_amount = float(self.transaction_amount_edit.text())
        except ValueError: # When Attempt fails
            result = QMessageBox.information(self, "Invalid Data",
                                             "Amount must be numeric",
                                             QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.transaction_amount_edit.setFocus()
                return
        
        try: # Attempts to apply transaction
            if self.sender() is self.deposit_button:
                transaction = "Deposit"
                self.__account.deposit(transaction_amount)
            elif self.sender() is self.withdraw_button:
                transaction = "Withdraw"
                self.__account.withdraw(transaction_amount)
            self.balance_label.setText(str(self.__account.balance))
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            self.balance_updated.emit(self.__account) # Sends Signal to Update Account
        except ValueError as e: # When Attempt fails
            result = QMessageBox.information(self, f"{transaction}", f"{e}",
                                             QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.transaction_amount_edit.setText("")
                self.transaction_amount_edit.setFocus()
                return

    @Slot()
    def __on_exit(self):
        self.close()