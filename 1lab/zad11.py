def frange(one, six, step):
    while one < six:
        yield round(one, 1)
        one += step
for x in frange(1, 6, 0.2):
    print(x, end="   ")