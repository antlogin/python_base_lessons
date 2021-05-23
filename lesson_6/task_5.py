class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        if self.title != "Pen":
            print("Это не ручка!")
        else:
            print("Это ручка!")


class Pencil(Stationery):
    def draw(self):
        if self.title != "Pencil":
            print("Это не карандаш!")
        else:
            print("Это карандаш!")


class Handle(Stationery):
    def draw(self):
        if self.title != "Handle":
            print("Это не маркер!")
        else:
            print("Это маркер!")


tmp1 = Stationery("Pen")
tmp1.draw()
tmp2 = Pen("Ручка")
tmp2.draw()
tmp3 = Pen("Pen")
tmp3.draw()
tmp4 = Pencil("Карандаш")
tmp4.draw()
tmp5 = Pencil("Pencil")
tmp5.draw()
tmp6 = Handle("Маркер")
tmp6.draw()
tmp7 = Handle("Handle")
tmp7.draw()
