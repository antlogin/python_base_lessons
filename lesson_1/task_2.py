user_data = int(input("Введите время в секундах: "))
seconds = user_data % 60
minutes = user_data // 60
hours = minutes // 60
minutes = minutes % 60
if hours > 99:
    print("Невозможно отобразить в формате чч:мм:сс, т.к. число часов содержит более двух цифр")
    print("%i:%02i:%02i" % (hours, minutes, seconds))
else:
    print("%02i:%02i:%02i" % (hours, minutes, seconds))





