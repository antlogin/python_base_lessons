start_list = [7, 1, 8, 3, 8, 5]
start_list.append(int(input('Введите целое число: ')))
start_list.sort(reverse=True)
del start_list[-1]
print(start_list)
