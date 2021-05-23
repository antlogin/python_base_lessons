input_nomber = int(input("Введите целое положительное число: "))
switch = True
max_nomber = 0
while switch:
    if input_nomber % 10 > max_nomber:
        max_nomber = input_nomber % 10
    if input_nomber % 10 == 9:
        break
    input_nomber = input_nomber // 10
    if input_nomber == 0:
        switch = False
print("Максимальная цифра в введенном числе: ", max_nomber)
