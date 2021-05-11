def my_quotient(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Делить на 0 нельзя!"


try:
    number_1 = float(input("Введите первое число: "))
    try:
        number_2 = float(input("Введите второе число: "))
        print("Результат: ", my_quotient(number_1, number_2))
    except ValueError:
        print("Введенное не является числом!")
except ValueError:
    print("Введенное не является числом!")
