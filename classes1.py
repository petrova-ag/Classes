class Animals:
    animals_weight = {}

    def __init__(self, kind, name, weight):
        self.kind = kind
        self.name = name
        self.weight = weight
        Animals.animals_weight[self.kind, self.name] = self.weight

    def feed(self):
        return 'Животные покормлены.'

    def whole_weight(self):
        #print(Animals.animals_weight)
        print(f'Общий вес всех животных {sum(Animals.animals_weight.values())}')
        max_weight = max(Animals.animals_weight.values())
        for keys, values in Animals.animals_weight.items():
            if values == max_weight:
                print(f'Самое тяжелое животное - {keys[0].lower()} {keys[1]}, вес {max_weight} кг.')


class Goose(Animals):
    kind = 'Гусь'

    def eggs(self):
        return 'Яйца собраны.'

    def sound(self):
        return 'Га-га-га'


class Cows(Animals):
    kind = 'Корова'

    def get_milk(self):
        return f'{self.kind} подоена.'

    def sound(self):
        return 'Му-му-му'


class Sheep(Animals):
    kind = 'Овца'

    def cut(self):
        return f'{self.kind} подстрижена.'

    def sound(self):
        return 'Бе-бе-бе'


class Chicken(Goose):
    kind = 'Курица'

    def sound(self):
        return 'Ко-ко-ко'


class Goats(Cows):
    kind = 'Коза'

    def sound(self):
        return 'Ме-ме-ме'


class Ducks(Goose):
    kind = 'Утка'

    def sound(self):
        return 'Кря-кря-кря'


goose_grey = Goose('Гусь', 'Серый', 10)
goose_white = Goose('Гусь', 'Белый', 10)

cow = Cows('Корова', 'Манька', 130)

sheep1 = Sheep('Овца', 'Барашек', 68)
sheep2 = Sheep('Овца', 'Кудрявый', 90)

chicken1 = Chicken('Курица', 'Ко-ко', 3)
chicken2 = Chicken('Курица', 'Кукареку', 2.5)

goat1 = Goats('Коза', 'Рога', 56)
goat2 = Goats('Коза', 'Копыта', 65)

duck = Ducks('Утка', 'Кряква', 1.5)
# print(Ducks.mro())

goose_grey.whole_weight()









