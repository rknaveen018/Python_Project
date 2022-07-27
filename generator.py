def even(i):
    for j in i:
        if j % 2 == 0:
            yield j
        else:
            pass


num = [0, 1, 2, 3, 4, 5]
gen = (even(num))

try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

except StopIteration:
    print("Generator reach at end")
