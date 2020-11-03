

from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


m = 0
for el in cycle(['ABC', 123, True]):
    if m > 10:
        break
    print(el)
    m += 1