"""Banking Chatbot with Intentional Security Vulnerabilities"""

__author__ = "Keith Robles"
__version__ = "3.19.2025"

# Code review in progress - security vulnerabilities identified

API_KEY = "sk_live_1234567890abcdef" 

ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
} 

VALID_TASKS = ["balance", "deposit", "exit"]

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! Let's get chatting!")

    chatting_with_bot = True
    while chatting_with_bot is True:  
        try:
            task = get_task()                
            if task in VALID_TASKS:                
                if task == "exit":
                    print(f"Thank you for banking with {COMPANY_NAME}.")
                    chatting_with_bot = False
                else:
                    account_number = get_account_number()
                    
                    if task == "deposit":
                        amount = get_amount()
                        result = make_deposit(account_number, amount)
                        print(result)
                    
                    elif task == "balance":
                        balance = get_balance(account_number)
                        print(balance)
                        log_transaction(account_number, f"Balance checked: {balance}")

        except Exception as e:
            print(f"Error: {e}") 


def get_account_number() -> int:
    account_number = input("Please enter your account number: ")
    

    if not account_number.strip():
        raise ValueError("Account number cannot be empty")
    
    try:
        return int(account_number)
    except ValueError:
        raise TypeError(f"Invalid account number: {account_number}")

def get_amount() -> float:
    amount = input("Enter an amount: ")
    try:
        amount = float(amount)
    except ValueError:
        raise TypeError("Amount must be a numeric type.")

    if amount > 0:
        return amount
    else:
        raise ValueError("Amount must be a value greater than zero.")

def get_balance(account_number):
    if type(account_number) is int:
        if account_number in ACCOUNTS:
            balance = ACCOUNTS[account_number]["balance"]
            return f"Your current balance for account {account_number} is ${balance:,.2f}."
        else:
            raise ValueError("Account number entered does not exist.")
    else:
        raise TypeError("Account number must be an int type.")

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
        ACCOUNTS[account_number]["balance"] += amount
        return f"You deposited ${amount:,.2f} to account {account_number}."

def get_task() -> str:
    task = input("What would you like to do (balance/deposit/exit)?: ").lower()
    if task in VALID_TASKS:
        return task
    else:
        raise ValueError(f'"{task}" is an unknown task.')

def log_transaction(account_number, message):
    import datetime
    log_entry = f"{datetime.datetime.now()}: Account {account_number} - {message}"
    print(f"[LOG] {log_entry}")

if __name__ == "__main__":
    chatbot()
