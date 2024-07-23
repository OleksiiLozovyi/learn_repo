# 1. У Джо Палуки товсті пальці, тому він завжди натискає клавішу "Caps Lock", коли насправді має намір натиснути клавішу "a".
# (Коли Джо намагається ввести якусь акцентовану версію "a", яка потребує більше натискань клавіш для створення акцентів,
# він більш обережний у присутності таких рафінованих символів ([Shift] + [a]) і буде натискати клавіші правильно).
# Обчисліть і виведіть результат введення Джо заданого тексту. Клавіша "Caps Lock" впливає лише на клавіші з літерами
# від "a" до "z", і не впливає на інші клавіші або символи. вважається, що клавіша "Caps Lock" спочатку вимкнена.
# assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
# assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
# assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"


def caps_lock(string):
    res_string = ''
    caps_flag = False
    for char in string:
        if char == 'a':
            caps_flag = not caps_flag
            continue
        if caps_flag:
            res_string += char.upper()
        else:
            res_string += char
    return res_string


def caps_lock(string):
    string_list = string.split('a')

    for i in range(1, len(string_list), 2):
        string_list[i] = string_list[i].upper()
    return ''.join(string_list)


assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"