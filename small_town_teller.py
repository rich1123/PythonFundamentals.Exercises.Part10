class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

#     # unique_cust = class Person()
#     #     obj = my_class
    #     if obj:
    #         print("Available")
    #     else:
    #         print("Not available")


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
#
#
class Account:
    def __init__(self, number, acc_type, owner):
        self.number = number
        self.type = acc_type
        self.owner = owner
#         self.balance = balance
#
#     def unique_number(self):
#         bank_numbers = []
#         for i in self.number:
#             if i not in bank_numbers:
#                 bank_numbers.append(i)
#
#     # number =
#     # type =
#     # owner =
#     # balance =
#


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = {}

        # Adding a customer to the bank
    def add_customer(self, person):
        self.customers.append(person.id)

    def add_account(self, account):
        if account in self.accounts:
            if account not in self.accounts:
                self.accounts[account.acc_type] = account.acc_type
                print("Account type:" + account.acc_type)
            else:
                print('Please try a different type')
        # Adding an account to the bank
        # Removing an
        # account from the bank
        # self.deposit = deposit # Depositing money into an account
        # self.withdrawal = withdrawal # Withdrawing money from an account
        # self.balance_inquiry = balance_inquiry # Balance inquiry for a particular self.account


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

bob_savings = Account(1001, "SAVINGS", bob)
#
# zc_bank.balance_inquiry(1001)
# # # 0
# zc_bank.deposit(1001, 256.02)
# zc_bank.balance_inquiry(1001)
# # 256.02
# zc_bank.withdrawal(1001, 128)
# zc_bank.balance_inquiry(1001)

zc_bank.add_account(bob_savings)
zc_bank.add_account(bob_savings)
