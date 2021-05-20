from itertools import count


def my_gen():
    factorial = 1
    for n in count(1):
        factorial *= n
        yield factorial


k = 1
for el in my_gen():
    print(f'Факториал {k}: {el}')
    if k == 5:
        break
    k += 1
