# Вам дано два рядки зі словами, розділеними комами. Спробуйте знайти, що спільного між цими рядками.
# Слова в одному рядку не повторюються.
# Ваша функція повинна знайти всі слова, які зустрічаються в обох рядках. Результат повинен бути представлений у
# вигляді рядка слів, відокремлених комами в алфавітному порядку.
# Вхідні дані: Два аргументи у вигляді рядків (str).
# Вихідні дані: Спільні слова у вигляді рядка (str).
# Приклади:
# assert checkio("hello,world", "hello,earth") == "hello"
# assert checkio("one,two,three", "four,five,six") == ""
# assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

def checkio(string_1, string_2):
    string_1 = string_1.split(',')
    string_2 = string_2.split(',')
    string = sorted(set(string_1) & set(string_2))
    return ',',json(string)