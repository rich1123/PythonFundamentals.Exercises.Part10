from typing import Dict


class Person:

    def __init__(self, id: int, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

#     # unique_cust = class Person()
#     #     obj = my_class
    #     if obj:
    #         print("Available")
    #     else:
    #         print("Not available")

    def __str__(self):
        return f"id: {self.id}. owner: {self.first_name} {self.last_name}"

# class myClass(object):
#     def __init__(self):
#         self.lis1 = []
#         self.dict1 = {}
#
#     def __nonzero__(self):
#         return bool(self.lis1 or self.dict1)
#
#     def unique_id(self):
#         bank_ids = []
#         for i in self.id:
#             if i not in bank_ids:
#                 bank_ids.append(i)
#         print(bank_ids)
#
#         def unique_owner(self):
#             self.owner = self.first_name + self.last_name
#             bank_owners = []
#             for i in self.owner:
#                 if i not in bank_owners:
#                     bank_owners.append(i)


class Account:

    def __init__(self, number, acc_type, account_owner):
        self.number: int = number
        self.type: str = acc_type
        self.owner: Person = account_owner
        self.balance: float = 0

    def __str__(self):
        return f"id: {self.number}. type: {self.type}. balance: {self.balance}"
#     def unique_number(self):
#         bank_numbers = []
#         for i in self.number:
#             if i not in bank_numbers:
#                 bank_numbers.append(i)


class Bank:

    def __init__(self):
        self.customers: list = []
        self.accounts: dict = {}

        # Adding a customer to the bank
    def add_customer(self, person: Person) -> None:
        if person.id in self.customers:
            raise ValueError(f"Customer with id {person.id} already exists.")
        else:
            self.customers.append(person.id)

    def add_account(self, account: Account) -> None:
        if account in self.customers:
            raise ValueError(f"Customer with id {account.number} already exists.")
        else:
            self.accounts[account.number] = account.balance
            # print('Please try a different type')

    def remove_account(self, account):
        if account in self.accounts:
            del [self.accounts[account]]

    def deposit(self, account: int, amt: float):
        if account in self.accounts:
            # account = self.accounts.get(azccount)
            self.accounts[account] += amt
        # self.accounts[acct_num] = amt
            print('Deposited amount: ' + str(amt))
        # else:
        #     raise ValueError(f"Account {account} not valid.")

    def withdrawal(self, account: int, amt: float):
        if amt <= self.accounts[account]:
            self.accounts[account] -= amt
        else:
            print("Insufficient funds")

    def balance_inquiry(self, account: int):
        if account in self.accounts:
            print(f"Inquiry result: {self.accounts[account]}")

    def save_data(self):
        PersistenceUtils.write_pickle("customers.pickle", self.customers)
        PersistenceUtils.write_pickle("accounts.pickle", self.accounts)

    def load_data(self):
        self.customers = PersistenceUtils.load_pickle("customers.pickle")
        self.accounts = PersistenceUtils.load_pickle("accounts.pickle")
        # Balance inquiry for a particular self.account

# Adding an account to the bank
        # Removing an
        # account from the bank
        # self.deposit = deposit # Depositing money into an account
        # self.withdrawal = withdrawal # Withdrawing money from an account

# Constraints
# When attempting to register a customer, the customer id must be unique.
# When attempting to add an account, the user associated with said account must already registered as a customer.
# When attempting to add an account, the account number must be unique.


# from small_town_teller import Person, Account, Bank
#

zc_bank = Bank()
#
bob = Person(1, "Bob", "Smith")
#
zc_bank.add_customer(bob)
print(zc_bank.customers)
bob_savings = Account(1001, "SAVINGS", bob)
#
print(zc_bank.accounts)
zc_bank.balance_inquiry(1001)
# # # 0

zc_bank.balance_inquiry(1001)
# 256.02
zc_bank.withdrawal(1001, 128)
zc_bank.balance_inquiry(1001)

zc_bank.add_account(bob_savings)
zc_bank.add_account(bob_savings)
zc_bank.deposit(1001, 256.02)