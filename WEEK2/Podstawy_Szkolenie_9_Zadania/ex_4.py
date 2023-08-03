class BankAccount:
    def __init__(self, account_number_, account_owner_, account_balance_):

        self.account_number = account_number_
        self.account_owner = account_owner_
        self.account_balance = account_balance_

    def deposit(self, deposit_amount):

        deposit_fee = (deposit_amount/100) * 2
        self.account_balance += (deposit_amount - deposit_fee)
        print(f'Current balance: {self.account_balance}')

    def withdraw(self, withdraw_amount):
        if self.account_balance >= withdraw_amount:
            self.account_balance -= withdraw_amount
        else:
            print("You do not have enough funds in your account.")

        print(f'Current balance: {self.account_balance}')

    def change_ownership(self, new_owner):
        self.account_owner = new_owner
        print(f'Current owner: {self.account_owner}')

    def display(self):
        print(f'Account number: {self.account_number}')
        print(f'Account owner: {self.account_owner}')
        print(f'Account balance: {self.account_balance}')


def main():

    bank_user = BankAccount(1234567890, "John Smith", 50000)
    bank_user.deposit(10000)
    bank_user.withdraw(50000)
    bank_user.change_ownership("Billy Brown")
    bank_user.display()


if __name__ == "__main__":
    main()
