# DRY --> DONT REPEAT YOURSELF

from classes.mammal import Mammal
from classes.animal import Animal

class Dog(Mammal):

    def __init__(self, name, rested=False, is_good=True):
        super().__init__(name, rested)
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name} rested={self.rested})"

    def make_sound(self):
        return "woof arf"

    def sleep(self):
        super().sleep()
        print("ZZZZZZZZZZZZZZZZZZzzzzzZZZZZZZZZZZZ")

    def run_around(self):
        print("PANT AND WAG TAIL")