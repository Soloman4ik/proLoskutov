# -*- coding: utf-8 -*-
import random
from random import randint
import simple_draw as sd

sd.resolution = (1200, 600)
COLOR_WHITE = (255, 255, 255)
COLOR_DARK_RED = (127, 0, 0)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(100, 100)
# radius = 50
#
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, color=sd.COLOR_BLUE, width=2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код


def buble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=sd.COLOR_DARK_RED, width=2)


# point = sd.get_point(100, 100)
# buble(point=point, step=10)
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 100)
#     buble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
# for y in range (100,301,100):
#
#  for x in range(100, 1100, 100):
#     point = sd.get_point(x, y)
#     buble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

for _ in range(100):
    point = sd.random_point()
    step = randint(1, 10)
    buble(point=point, step=step)
sd.pause()