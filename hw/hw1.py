class Animal:

    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def mood(self):
        return f"{self.name} I'm hungry!"
    def run(self, increase):
        self.speed += increase
        return f"{self.name} is running faster! New speed:{self.speed}"

cheetah = Animal("Cheetah",2,150)
elephant = Animal("Elephant",9, 20)

print(cheetah.mood())
print(elephant.mood())

print(cheetah.run(30))
print(elephant.run(5))