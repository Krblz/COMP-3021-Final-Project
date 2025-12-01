__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Keith Robles"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from PySide6.QtCore import Slot

class ClientLookupWindow(LookupWindow):
    """
    EventHandler Class
    """
    def __init__(self):
        """
        Initializes an instance of ClientLookupWindow
        """
        super().__init__()
        # Loads and Sets Values of client_listing and accounts
        data = load_data()
        self.__client_listing = data[0]
        self.__accounts = data[1]

        # Signals
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

    @Slot()
    def __on_lookup_client(self) -> None:
        # Obtains Client Information
        try: 
            client_number = int(self.client_number_edit.text())
        except ValueError:
            result = QMessageBox.information(self, "Input Error", 
                                             "The client number must be numeric.",
                                             QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.reset_display()
                return
        try:
            client = self.__client_listing[client_number]
        except KeyError: 
            result = QMessageBox.information(self, "Not Found",
                                             "Client number: " +
                                             f"{client_number} not found.",
                                             QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.reset_display()
                return

        # Display Data to the screen
        self.client_info_label.setText(f"Client Name: {client.first_name} " +
                                       f"{client.last_name}")
        

        for account in self.__accounts.values():
            row_position = self.account_table.rowCount() # Checks for Row Count 
            if account.client_number == client.client_number:
                self.account_table.insertRow(row_position) # Adds new Row
                # Converts each data into a str for setItem
                acc_num = str(account.account_number)
                acc_num_item = QTableWidgetItem(acc_num)
                balance = str(account.balance)
                bal_item = QTableWidgetItem(balance)
                date_created = str(account._date_created)
                d_created_item = QTableWidgetItem(date_created)
                account_type = str(account.__class__.__name__) # Checks for the BankAccount Classes
                acc_type_item = QTableWidgetItem(account_type)
                # Sets the Item Contents
                self.account_table.setItem(row_position, 0, acc_num_item)
                self.account_table.setItem(row_position, 1, bal_item)
                self.account_table.setItem(row_position, 2, d_created_item)
                self.account_table.setItem(row_position, 3, acc_type_item)
                # Resizes the Columns to fit contents
                self.account_table.resizeColumnsToContents()
    
    @Slot()
    def __on_text_changed(self) -> None:
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        if self.account_table.item(row, 0) is not None:
            account_number = int(self.account_table.item(row, 0).text())
            if account_number in self.__accounts:
                bank_account = self.__accounts[account_number]
                account_details = AccountDetailsWindow(bank_account)
                account_details.balance_updated.connect(self.__update_data)
                account_details.exec_()
            else:
                result = QMessageBox.information(self, "No Bank Account",
                                             "Bank Account selected does not exist",
                                             QMessageBox.Ok)
                if result == QMessageBox.Ok:
                    self.reset_display()
                    return
        else:
            result = QMessageBox.information(self, "Invalid Selection",
                                             "Please select a valid record.",
                                             QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.reset_display()
                return

    @Slot(BankAccount)        
    def __update_data(self, account: BankAccount) -> None:
        for row in range(self.account_table.rowCount()):
            target_acc_num = account.account_number              # Target Account Number
            curr_acc_num = int(self.account_table.item(row, 0).text())  # Current Account Number in Row
            if target_acc_num == curr_acc_num:
                balance = str(account.balance)
                bal_item = QTableWidgetItem(balance)
                self.account_table.setItem(row, 1, bal_item)
                self.__accounts[target_acc_num]._balance = account.balance
                update_data(account)

