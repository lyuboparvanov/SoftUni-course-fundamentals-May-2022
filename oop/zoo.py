class Zoo:
    _animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        zoo._animals += 1
    def get_info(self, species):
        if species == 'mammal':
            print(f"Mammals in {zoo.name}: {', '.join(zoo.mammals)}")
        elif species == 'fish':
            print(f"Fishes in {zoo.name}: {', '.join(zoo.fishes)}")
        elif species == 'bird':
            print(f"Birds in {zoo.name}: {', '.join(zoo.birds)}")
        print(f"Total animals: {zoo._animals}")
name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_animals = int(input())

for _ in range(number_of_animals):
    command = input().split()
    class_of_animal = command[0]
    name_of_animal = command[1]
    zoo.add_animal(class_of_animal, name_of_animal)

type_of_species = input()
zoo.get_info(type_of_species)
