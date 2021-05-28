from abc import ABC, abstractmethod


class Clothes(ABC):
    tissue_summ = 0
    single_thing = True

    def __init__(self, n, s):
        self.name = n
        self.size = s

    def __add__(self, other):
        Clothes.single_thing = False
        Clothes.tissue_summ = Clothes.tissue_summ + self.tissue_consumption + other.tissue_consumption
        return Blank("", 0)

    def __str__(self):
        result = 0
        if Clothes.single_thing == False:
            result = self.tissue_summ
            self.tissue_summ = 0
            return f"{result}"
        else:
            result = self.tissue_consumption
            return f"{result}"

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass


class Blank(Clothes):

    @property
    def tissue_consumption(self):
        return self.size


class Costume(Clothes):

    @property
    def tissue_consumption(self):
        return round(2 * self.size / 100 + 0.3, 2)  # 3,7


class Coat(Clothes):

    @property
    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)  # 6,5


palto = Coat("gggg", 39)
kostum = Costume("DDDd", 170)

print(kostum)
print(palto)
print(kostum + palto + palto)
