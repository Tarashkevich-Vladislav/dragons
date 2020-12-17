from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    dragons_colours = ['зелёный', 'чёрный', 'красный']
    for dragon in dragon_list:
        if dragon._color in dragons_colours:
            print('Вышел', dragon._color, 'дракон!')
        else:
            print('Гадкий', dragon._color ,'тролль выскочил из кустов!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            if (dragon._color == 'множащийся в глазах'):
                answer = input()
            else:
                answer = annoying_input_int('Ответ:')
            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** твой враг кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Неприятель', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и троллями!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 6
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 6)
        print('У Вас на пути', dragon_number, 'драконов или троллей!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
