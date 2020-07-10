def incremento():
    n1 = 0
    while True:
        n1 += 1
        yield n1

na = incremento()
while int(na) < 20:
    print(next(na))