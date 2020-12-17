from gameunit import *

class Hero(Attacker):
    def __init__(self, name):
        self._name = name
        self._experience = 0
        self._health = 100
        self._attack = 50

    def attack(self, target):
        target._health -= self._attack
# атака 50, здоровье 100, опыт 0, имя задаваемое, пробитие уроном на атаку
