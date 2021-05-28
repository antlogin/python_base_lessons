f = open("text_3.txt", 'r', encoding="utf-8")
arr_str = []
N_str = 0
avr_salary = 0
while True:
    content = f.readline()
    if content:
        content = content.rstrip()
        arr_str.append(content.split(" "))
        N_str += 1
    else:
        break
i = 0
print("Список сотрудников с зарплатой < 20000:")
while i < N_str:
    if float(arr_str[i][1]) < 20000:
        print(arr_str[i][0])
    avr_salary = avr_salary + float(arr_str[i][1])
    i += 1
print('Средняя зарплата всех сотрудников равна:', avr_salary / N_str)
f.close()
