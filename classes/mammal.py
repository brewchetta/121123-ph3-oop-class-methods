from classes.animal import Animal

class Mammal(Animal):

    def __init__(self, name, rested=False):
        self.name = name
        self.rested = rested

    def __repr__(self):
        return f"Mammal(name={self.name})"

    def make_sound(self):
        return "generic mammal sound"

    def sleep(self):
        self.rested = True

    def run_around(self):
        self.rested = False
