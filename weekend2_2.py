# 3.Дан рядок.
# НАйдіть в ньому другу букву "а". Виведіть індекс.
# Якщо є тільки одна  - виведить "alone", якщо взагалі нема
# виведіть None

# line = 'ablabla bla'
# if line.count('a') == 1:
#     print('Alone')
# elif line.count('a') == 0:
#     print(None)
# else:
#     print(line.find('a', line.find('a')+1))




line = 'ablabla bla'
match line.count('a'):
    case 1:
        print('Alone')
    case 0:
        print(None)
    case _:
        print(line.find('a', line.find('a')+1))