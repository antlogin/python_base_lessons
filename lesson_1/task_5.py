# не сумел придумать, как проверить вводимые значения на соответствие типу float...
print("Все вводимые значения должны быть числами.")
proceeds = float(input("Введите выручку: "))
cost = float(input("Введите величину издержек: "))
if proceeds > cost:
    print("Вы зарабатываете!!!")
    print("Ваш доход: ", proceeds - cost)
    print("Рентабельность: ", (proceeds - cost) / proceeds)
    staf_nomber = float(input("Введите число сотрудников: "))
    print("Доход на одного сотрудника: ", (proceeds - cost) / staf_nomber)

elif proceeds == cost:
    print("Ваш доход = 0")
else:
    print("Вы теряете деньги...")
