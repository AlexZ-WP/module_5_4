# class House:
#
#     houses_history = []
#
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
#
# h1= House('date', second= 25, third = 3.14)

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # nf = [i for i in range(1, new_floor+1)] # генератор списка для создания произвольного списка целых чисел
        nf = list(range(1, new_floor + 1))
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            print(*nf[:], sep="\n")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # if isinstance(other, int) and isinstance(other, House):

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
