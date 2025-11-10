# class Test:
#
#     # double underline
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name

# int_test = 123
# int_test2 = 1234
#
# print(int_test > int_test2)

# test_obj = Test("test")
#
# print(test_obj)
#
#
# print(test_obj)



class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.array = array

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.y > other.x

    def __getitem__(self, item):
        return self.array[item]

obj_1 = Vector(1, 2 [1, 2, 3])
obj_2 = Vector(3, 4)
print(obj_1 < obj_2)
