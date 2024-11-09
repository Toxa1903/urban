class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            new_floors = self.floors + value
            return House(self.name, new_floors)
        elif isinstance(value, House):
            new_floors = self.floors + value.floors
            return House(self.name, new_floors)
        return NotImplemented

    def __radd__(self, value):

        return self.__add__(value)

    def __iadd__(self, value):
        # __iadd__ is for in-place addition
        if isinstance(value, int):
            self.floors += value
            return self
        elif isinstance(value, House):
            self.floors += value.floors
            return self
        return NotImplemented

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # eq

h1 = h1 + 10  # add
print(h1)
print(h1 == h2)

h1 += 10  # iadd
print(h1)

h2 = 10 + h2  # radd
print(h2)

print(h1 > h2)  # gt
print(h1 >= h2)  # ge
print(h1 < h2)  # lt
print(h1 <= h2)  # le
print(h1 != h2)  # ne
