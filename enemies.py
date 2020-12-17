from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
        
class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'
    
    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
        
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 50
        self._attack = 25
        self._color = 'чёрный'
    
    def question(self):
        x = randint(1, 20)
        y = randint(1, 20)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class ChaoticTroll(Troll):
	def __init__(self):
		self._health = 50
		self._attack = 75
		self._color = 'хаотический'

	def question(self):
		x = randint(1, 5)
		self.__quest = 'Угадай случайное число от 1 до 5'
		self.set_answer(x)
		return self.__quest

class PrimalTroll(Troll):
	def __init__(self):
		self._health = 50
		self._attack = 75
		self._color = 'простой'

	def __isPrime(self, x):
		i = 2
		while i * i <= x:
			if x % i == 0:
				return 0
			i += 1
		return 1

	def question(self):
		x = randint(1, 101)
		self.__quest = 'Является ли число ' + str(x) + ' простым?(Если да, то введи 1, иначе введи 0)'
		self.set_answer(self.__isPrime(x))
		return self.__quest

class MultiTroll(Troll):
	def __init__(self):
		self._health = 50
		self._attack = 75
		self._color = 'множащийся в глазах'

	def __allMultiplyers(self, x):
		result = []
		for i in range(1, x+1):
			if x % i == 0:
				result.append(str(i))
		return ",".join(result)

	def question(self):
		x = randint(1, 20)
		self.__quest = 'Введи мне все множители числа в порядке возрастания ' + str(x) + '. Например, для числа 2 нужно ввести: 1,2(с запятой без пробелов)'
		self.set_answer(self.__allMultiplyers(x))
		return self.__quest

enemy_types = [GreenDragon, RedDragon, BlackDragon, ChaoticTroll, PrimalTroll, MultiTroll]
