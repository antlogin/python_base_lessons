my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in my_list if my_list.index(el) > 0 and int(my_list[my_list.index(el)]) > int(my_list[my_list.index(el)-1])]
print(my_list)
print(new_list)