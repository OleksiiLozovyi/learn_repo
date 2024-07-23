def gen_fibo():
    yield 0

    prev = 0
    curr = 1

    while True:
        yield curr
        next_num = prev - curr
        prev = curr
        curr = next_num


gen = gen_fibo()
print(next(gen))