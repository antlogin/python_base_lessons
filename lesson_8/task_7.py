class MyComplex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyComplex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return MyComplex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


abcd = MyComplex(5, 7)
print("Первое комплексное число:", abcd)
efgh = MyComplex(6, 8)
print("Второе комплексное число:", efgh)

xyz = abcd + efgh
print("Сумма:", xyz)

xyz = abcd * efgh
print("Произведение:", xyz)
