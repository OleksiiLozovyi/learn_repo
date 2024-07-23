class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def info(self):
        return f"{self.nickname}-{self.weight}"

class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def say(self):
        return "Meow"


class DogCat(Dog, Cat):
    def say(self):
        return "Woof"


catdog = CatDog("Mur", 3)
dogcat = DogCat("Bob", 7)

print(catdog.say())
print(catdog.info())

print(dogcat.say())
print(dogcat.info())
