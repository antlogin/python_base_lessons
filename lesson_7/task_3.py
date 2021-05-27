# from abc import ABC, abstractmethod


class Cell:
    def __init__(self, N):
        self.number_el = N

    def __add__(self, other):
        sum = int(self.number_el) + int(other.number_el)
        return Cell(sum)

    def __sub__(self, other):
        sub = int(self.number_el) - int(other.number_el)
        if sub > 0:
            return Cell(sub)
        else:
            print("В первой клетке мало элементов")
            return Cell(0)

    def __mul__(self, other):
        mul = int(self.number_el) * int(other.number_el)
        return Cell(mul)

    def __truediv__(self, other):
        mul = int(self.number_el) // int(other.number_el)
        return Cell(mul)

    def __str__(self):
        tmp = self.number_el
        return f"{tmp}"

    def make_order(self, n):
        j = 1
        k = 1
        output_str = ""
        while j <= self.number_el:
            output_str = output_str + "*"
            if k >= n:
                output_str = output_str + "\n"
                k = 0
            j += 1
            k += 1
        return output_str


tmp1 = Cell(17)
tmp2 = Cell(18)
tmp3 = tmp1 - tmp2
print(tmp3.make_order(4))
