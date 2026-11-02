class Account:
    def __init__(self, name, balabce):
        self.name = name
        self.balance = balabce
    
    def display_balance(self) -> None:
        print(f"Balance: ${self.balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
