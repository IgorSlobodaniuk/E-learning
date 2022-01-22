PLACES = {
    'forest': [],
    'field': [],
    'home': [],
}


# Incorrect
class Animal:
    def select_animal_place(self, animal):
        if animal == 'Bear':
            self.send_to_forest(animal)
        elif animal == 'Cat':
            self.send_to_home(animal)
        elif animal == 'Fox':
            self.send_to_field(animal)

    def send_to_forest(self, animal):
        PLACES['forest'].append(animal)

    def send_to_field(self, animal):
        PLACES['field'].append(animal)

    def send_to_home(self, animal):
        PLACES['home'].append(animal)


# Correct

class Animal:
    animal = None
    place = None

    def send_animal(self):
        PLACES[self.place] = self.animal


class ForesAnimal:
    animal = 'Bear'
    place = 'forest'


class FieldAnimal:
    animal = 'Fox'
    place = 'field'


class HomeAnimal:
    animal = 'Cat'
    place = 'home'
