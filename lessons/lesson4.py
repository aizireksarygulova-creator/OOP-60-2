# class Test:
#
#     # double underline
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# test_obj = Test("test")
# test_str = "123"
# print(test_obj)

# int_test = 123
# int_test2 = 1234

# print(int_test > int_test2)




# class Vector:
#     def __init__(self, x, y, array):
#         self.x = x
#         self.y = y
#         self.array = array
#
#     def __lt__(self, other):# знак <
#         return self.x < other.x
#
#     def __gt__(self, other):# знак >
#         return self.y > other.x
#
#     def __getitem__(self, item):
#         return self.array[item]
#
#
# class MyList:
#     def __init__(self, value):
#         self.value = value
#
#     def __getitem__(self, item):
#         return self.value[item]
#
# my_list = MyList([1, 2, 3])
# origin_list = [1, 2, 3]
# print(my_list[2])
# print(origin_list[2])
#
# # obj_1 = Vector(1, 2, [1, 2, 3] )
# # # obj_2 = Vector(3, 4)
# # # obj_3 = Vector(3, 4)
# # print(obj_1[2])

# class Money:
#
#     def __init__(self, sum, currency):
#         self.sum = sum
#         self.currency = currency
#
#     #==
#     def __eq__(self, other):
#
#         if self.currency == other.currency:
#             return True
#         else:
#             return False
#
#     def __add__(self, other):
#         if self.currency == other.currency:
#             return self.sum + other.sum
#         else:
#             return f"Валюты не равны {self.currency} {other.currency}"
#
# SOM = Money(100, "SOM")
# USD = Money(100, "USD")
#
# print(SOM + USD)
#

class BankAccount:
    # Атрибута класса
    bank_name = "Simba"

    def __init__(self, first_name, last_name, balance):
        # Атрибута экземпляра класса
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def get_name(self):
        return self.first_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @staticmethod
    def calculate_deposit():
        return 123

ardager = BankAccount("Ardager", "Kartanbekov", 100000)
john = BankAccount("John", "Doe", 999)

# print(ardager.first_name)
# print(john.get_name())

print(john.full_name)






# print(BankAccount.get_balance())
#
# # print(BankAccount.get_bank_name())
# # print(BankAccount.get_name())
#
#
# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     @staticmethod
#     def calculate_deposit(amount, procent):
#         return amount * procent
#
# print(Bank.calculate_deposit(12, 2))
#
#
#
#
