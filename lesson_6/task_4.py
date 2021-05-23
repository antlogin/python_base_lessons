class Car:
    def __init__(self, sp, col, n, is_p):
        self.speed = sp
        self.color = col
        self.name = n
        self.is_police = is_p

    def go(self):
        if self.speed != 0:
            print("Машина едет")

    def stop(self):
        if self.speed == 0:
            print("Машина стоит")

    def turn(self):
        print("Машина повернула")

    def show_speed(self):
        print("Скорость машины: ", self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!!!")
        else:
            print("Скорость машины: ", self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!!!")
        else:
            print("Скорость машины: ", self.speed)


class PoliceCar(Car):
    pass


lada = TownCar(50, "Red", "Лада", False)
lada.go()
lada.stop()
lada.turn()
lada.show_speed()
lada.speed = 70
lada.show_speed()

print()
ford = PoliceCar(100, "Blue", "Форд", True)
ford.show_speed()
print()
porter = WorkCar(50, "White>", "Портер", False)
porter.show_speed()
