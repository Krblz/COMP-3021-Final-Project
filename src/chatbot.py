"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Keith Robles"
__version__ = "3.19.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    chatting_with_bot = True
    while chatting_with_bot is True:  

        try:
            # Get the Task
            task = get_task()                
            if task in VALID_TASKS:                
                if task == "exit":
                    # Print thank you message
                    print(f"Thank you for banking with {COMPANY_NAME}.")
                    chatting_with_bot = False
                else:
                    # Asks for Account Number
                    account_number = get_account_number()
                    # Asks for Amount to Deposit
                    if task == "deposit":
                        amount = get_amount()
                        make_deposit(account_number, amount)
                        balance = get_balance(account_number)
                    # Get current Balance of Account                      
                    elif task == "balance":
                        balance = get_balance(account_number)

                    # Shows current Balance of Account    
                    print(balance)

        # Handles Exception and Displays Exception Message
        except Exception as e:
            print(e)
        


# Gets the account number
def get_account_number() -> int:
    account_number = input("Please enter your account number: ")
    result = ""

    try:
        account_number = int(account_number)
    except ValueError:
        raise TypeError("Account number must be an int type.")

    if account_number in ACCOUNTS:
        #print("Valid")
        result = account_number
    else:
        raise ValueError("Account number entered does not exist.")
                
    return result

# Gets the Amount
def get_amount() -> float:
    amount = input("Enter an amount: ")
    result = ""

    try:
        amount = float(amount)
    # When Converting Non-Float to String, It always raises a ValueError
    # This Converts the ValueError into a TypeError because Assignment Instructions
    # Is Asking for a TypeError when a Non-Numeric Type is inputted
    except ValueError:
        raise TypeError("Amount must be a numeric type.")

    if amount > 0:
        #print("Valid")
        result = amount
    else:
        raise ValueError("Amount must be a value greater than zero.")    
    
    return result

# Gets the Balance    
def get_balance(account_number):
    # Boolean to check if account_number is int or not, defaults at False
    is_int = False

    # Checks if the account_number is already an int, converts, if not
    # if it can't be converted, raises a TypeError
    if type(account_number) is int:
        is_int = True
    elif account_number.isdigit():
        account_number = int(account_number)
        is_int = True
    else:
        raise TypeError("Account number must be an int type.")
    if is_int == True:
        if account_number in ACCOUNTS:
            account_balance = ACCOUNTS[account_number]["balance"]
            #print("Valid")
            result = f"Your current balance for account {account_number} is ${account_balance:,.2f}." 
        else:
            raise ValueError("Account number entered does not exist.")
    
    return result
    
# Makes the Deposit
def make_deposit(account_number, amount):
    if type(account_number) is not int:       
        raise TypeError("Account number must be an int type.")
    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")

    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Amount must be a numeric type.") 

    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    else:        
        ACCOUNTS[account_number]["balance"] = amount + ACCOUNTS[account_number]["balance"]
        result = f"You have made a deposit of ${amount:,.2f} to account {account_number}."
        
    #print(result)
    return result

# Prompts the user to input a task
def get_task() -> str:
    task = input("What would you like to do (balance/deposit/exit)?: ").lower()

    if task in VALID_TASKS:
        if task == "balance":
            result = task
        elif task == "deposit":
            result = task
        elif task == "exit":
            result = task
    else:
        raise ValueError(f'"{task}" is an unknown task.')
    
    return result

if __name__ == "__main__":
    chatbot()