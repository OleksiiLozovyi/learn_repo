# Дан рядок вида
# Hello Hi
# Bye Goodbye
# List Array
# Go Run
# Street Avenue
# де кожному рядку записані синоніми
# Створіть словник синонімів.
# Отримайте одне слово іnput-ом і знайдіть для нього синонім.


string = '''Hello Hi
Bye Goodbye
List Array
Go Run
Street Avenue'''

list_of_words = string.split()
dict_of_words = {}
for i in range(0, len(list_of_words), 2):
    dict_of_words[list_of_words[i].lower()] = list_of_words[i+1].lower()
    # dict_of_words[list_of_words[i+1].lower()] = list_of_words[i].lower()
your_word = input('Word: ')
print(dict_of_words.get(your_word, 'piska'))

ind = list(dict_of_words.values()).index(your_word)
print(list(dict_of_words)[ind])