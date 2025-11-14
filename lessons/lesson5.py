#1. Что такое декоратор?
# Декоратор - это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность

# class Person:
#
#     def simple_method(self):
#         pass
#
#     @staticmethod
#     def static_method(self):
#         pass
#
#     @classmethod
#     def class_method(cls):
#         pass


def simple_decorator(func):
    def wrapper():
        print("До выполнения!!")
        func()
        print("После выполнения!!")
    return wrapper

def test():
    return print('Test')
test()