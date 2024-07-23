class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(cls, color):
        cls.color = color


# Створення екземплярів об'єкта
first_animal = Animal("Buddy", 5)
second_animal = Animal("Milo", 7)

# Виклик методу change_color для зміни кольору на "red"
first_animal.change_color("red")

# Перевірка значення змінної класу color
print(Animal.color)         # Виведе: red
print(first_animal.color)   # Виведе: red
print(second_animal.color)  # Виведе: red