a = float(input("Введите стартовую дистанцию: "))
b = float(input("Введите целевую дистанцию: "))
day_nomber = 1
if b < a:
    print("Ошибка! Целевая дистанция меньше стартовой")
else:
    while a <= b:
        if a == b:
            break
        else:
            a += a/10
            day_nomber += 1
    print("Номер дня достижения цели = ", day_nomber)

