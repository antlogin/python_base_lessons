class Worker:

    def __init__(self, n, s_n, pos, inc_wage, inc_bonus):
        self._income = {"wage": inc_wage, "bonus": inc_bonus}
        self.name = n
        self.surname = s_n
        self.position = pos


class Position(Worker):

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


man = Position("Bob", "Dilan", "manager", 200, 33)
woman = Position("Liza", "Krauf", "boss", 400, 55)
man.get_full_name()
man.get_total_income()
print()
woman.get_full_name()
woman.get_total_income()
