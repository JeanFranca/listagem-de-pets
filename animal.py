class animal:
    def __init__(self, name, age, genre, species):
        self.name = name
        self.age = age
        self.genre = genre
        self.species = species
    
    def speak(self):
        print('%s diz: auau!' %self.name)
    
    def play(self):
        print('%s estendeu a patinha!' %self.name)