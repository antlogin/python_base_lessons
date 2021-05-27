class Matrix:
    def __init__(self, l_of_l):
        self.list_of_list = l_of_l

    def __str__(self):
        result_str = ""
        for i in range(len(self.list_of_list)):
            string_i = self.list_of_list[i]
            print()
            for j in range(len(string_i)):
                result_str = result_str + str("{:^8.2f}".format(string_i[j]))
            result_str = result_str + "\n"
        return result_str

    def __add__(self, other):
        new = []
        tmp = 0
        for i in range(len(self.list_of_list)):
            new.append([0] * len(self.list_of_list[0]))
        string_1 = sum(self.list_of_list, [])
        string_2 = sum(other.list_of_list, [])
        for i in range(len(self.list_of_list)):
            for j in range(len(self.list_of_list[0])):
                new[i][j] = float(string_1[tmp]) + float(string_2[tmp])
                tmp = tmp + 1
        obj = Matrix(new)
        return obj


my_matrix_1 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90], [70, 80, 90]])
my_matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]])
print(my_matrix_1 + my_matrix_2)
