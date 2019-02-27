class person:
    def __init__(self, name, age, genre):
        self.name = name
        self.age = age
        self.genre = genre
        self.pet = []

    def addpet(self, animal):
        self.pet.append(animal)
    
    