
from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as summa:
    summa.write(' '.join([str(randint(1, 100)) for _ in range(100)]))
    summa.seek(0)
    print(sum(map(int, summa.readline().split())))