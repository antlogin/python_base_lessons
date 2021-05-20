import time

class TrafficLight:
    # атрибуты класса
    __color = "red"

    # методы класса
    def  running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(5)


light = TrafficLight()
light.running()