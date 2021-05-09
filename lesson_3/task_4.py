def my_pow1(x, y):
    if x > 0 and y < 0 and float(y) == int(y):
        return 1 / x ** (-1 * y)
    else:
        return "Введены недопустимые значения аргументов"


def my_pow2(x, y):
    if x > 0 and y < 0 and float(y) == int(y):
        result = 1
        for i in range(-1 * y):
            result = result * x
        return 1 / result
    else:
        return "Введены недопустимые значения аргументов"


try:
    x_ = float(input("Введите положительное число x: "))
    y_ = int(input("Введите целое отрицательное число y: "))
    print("my_pow1: ", my_pow1(x_, y_))
    print("my_pow2: ", my_pow2(x_, y_))
except ValueError:
    print("Введены недопустимые значения аргументов")
