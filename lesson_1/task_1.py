true_password = 'ab777'
text_1 = "Введите первое число: "
text_2 = "Введите втроеое число: "
result_text = "Сумма = "
password = input('Введите пароль: ')
access = False
quotient = None
if password == true_password:
    print('Пароль принят, добро пожаловать в систему')
    access = True
    number_1 = int(input(text_1))
    number_2 = int(input(text_2))
    summ_ = number_1 + number_2
    quotient = number_1 / number_2
    print("Сумма чисел: ", summ_)
    print("Частное чисел: ", quotient)
if password != true_password:
    print('Пароль неверен, вход запрещен')
print("Тип переменной quotient: ", type(quotient))

