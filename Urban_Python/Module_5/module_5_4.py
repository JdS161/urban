class House:

    houses_history =[]

    def __new__(cls, *args, **kwargs):
        if args and isinstance(args[0], str):
            name = args[0]
            cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, _name, _number_of_floors):
        self.name = _name
        self.number_of_floors = _number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# Пример результата выполнения программы:
# Пример выполнения программы:
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