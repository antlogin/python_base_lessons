month_nomber = int(input('Введите номер месяца: '))
if month_nomber > 12 or month_nomber < 1:
    print('Месяца с таким номером не существует')
else:
    my_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
    for el in my_dict:
        if my_dict.get(el).count(month_nomber) == 1:
            print('Месяц с номером ', month_nomber, ' это ', el)
