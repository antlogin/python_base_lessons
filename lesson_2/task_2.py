my_list_length = input('Введите длину списка: ')
if not my_list_length.isdecimal():
    print('Введенное не является целым числом')
else:
    my_list = []
    i = 0
    while i < int(my_list_length):
        i += 1
        print('Введите элемент списка номер ', i, '- ', end='')
        my_list.append(input())
    i = 0
    tmp = None
    for k in my_list:
        if i % 2 == 1 and i < int(my_list_length):
            my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
        i += 1
    print(my_list)
