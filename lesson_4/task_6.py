from itertools import count
from itertools import cycle
# import itertools


for i in count(int(input('Введите число: '))):
    print(i)
    if i >= 10:
        break
n = 1
for el in cycle("XYZ"):
    if n == 5:
        break
    print(el)
    n += 1
