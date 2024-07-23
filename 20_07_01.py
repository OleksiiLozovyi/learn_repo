# В рядку написан текст.
# Для кожного слова підрахуйте
# кілька разів воно зустрічалось в цьому тексті.

import re



text = '''Little girl, little girl Why are you crying? Inside your restless soul your heart is dying Little one, little one
Your soul is purging Of love and razor blades Your blood is surging Runaway From the river to the street And find
yourself with your face in the gutter Your a stray for the salvation army There is no place like home When you got
no place to go Little girl, little girl Your life is calling The charlatans and saints of your abandon Little one
little one The sky is falling The lifeboat of deception is now sailing In the wake all the way No rhyme or reason
Your bloodshot eyes Will show your heart of treason Little girl little girl You dirty liar You're just a junkie
Preaching to the choir Runaway To your lost tranquility And find yourself with your face in the gutter Your a stray
for the dregs of humanity There is no place like home When you got no place to go The traces of blood Always follow
you home Like the Mascara tears From your getaway Your walking with blisters And running with shears So unholy. Sister
of grace. Runaway From the river to the street And find yourself with your face in the gutter You're a stray for the
salvation army There is no place like home When you got no place to go'''

words = re.split(r'[\?, \!, \n]',text.lower())
dict_of_works = {}
for word in words:
#     if word not in dict_of_works:
#         dict_of_works[word] = 1
#     else:
#         dict_of_works[word] = dict_of_works[word]+1
    dict_of_works[word] = dict_of_works.get(word, 0) + 1

new_dict = {}
for key, value in dict_of_works.items():
    new_dict[value] = new_dict.get(value, [])+[key, ]

for key in sorted(new_dict, reverse=True):
    print(f"{key}:{new_dict[key]}")


