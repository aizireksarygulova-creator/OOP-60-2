# Наследование

# Родительский класс\супер класс
class Hero:
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return self.name

class Skill:
    pass

# дочерний класс
class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp


    def action1(self):
        return f"Я потомок {self.name}"

class WarriorHero(MageHero):
    pass


obj_1 = Hero("Олег", 10, 100)
obj_2 = MageHero("Ardager", 10, 100, 50)
obj_3 = WarriorHero("Abob",10, 100, 50)

# print(obj_1.action())
# print(obj_2.action())
# print(obj_3.action1())



# class A:

    # def action(self):
#         return "A"
#
# class B(A):
#     def action(self):
#         return "B"
#
# class C(A):
#     def action(self):
#        print(super().action())
#
#
# class D(C, B):
#     ...
#     # def action(self):
#     #     return "D"
#
# obj_4 = D()
#
# print(D.__mro__)

class Animal:
    def action(self):
        return "Animal"

class Fly(Animal):
    def action(self):
        return  f"Fly"

class Swim(Animal):
    def action(self):
        return f"Swim"

class Duck(Swim, Fly):
    ...

duck = Duck()
print(duck.action())