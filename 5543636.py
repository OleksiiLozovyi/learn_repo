# Курець бросає палити.
# Він обіцяє собі кожень день палити на 10 % менше
# ніж в попередній день, округляючи до меншого.
# Зазвичай він випалює в день 30 цигарок.
# Через скільки днів він кине палити?


def smoke(sigarets=30):
    days = 0
    while sigarets > 0:
        sigarets = int(sigarets*0.9)
        days+= 1
    return days
smoke()
print(smoke())