class Road:
    __density = 25
    __number_of_layers = 5

    def __init__(self, len, wid):
        self._length = len
        self._width = wid
        print("Расход асфальта: ", self._length * self._width * self.__density * self.__number_of_layers / 1000, "т")


quantity = Road(5000, 20)