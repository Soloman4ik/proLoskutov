# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
sd.background_color = 210, 105, 30
sd.resolution = (600, 600)


def smile(x, y):
    point = sd.get_point(x, y)
    sd.circle(point, radius=80, color=sd.COLOR_YELLOW, width=5)
    aye = sd.get_point(x + 35, y + 20)
    sd.circle(aye, radius=15, color=sd.COLOR_YELLOW, width=2)
    aye = sd.get_point(x + 35, y + 20)
    sd.circle(aye, radius=5, color=sd.COLOR_YELLOW, width=0)
    aye = sd.get_point(x - 35, y + 20)
    sd.circle(aye, radius=15, color=sd.COLOR_YELLOW, width=2)
    aye = sd.get_point(x - 35, y + 20)
    sd.circle(aye, radius=5, color=sd.COLOR_DARK_RED, width=0)
    point_list = (sd.get_point(x - 40, y - 30), sd.get_point(x - 20, y - 40),
                  sd.get_point(x + 20, y - 40), sd.get_point(x + 40, y - 30))
    sd.lines(point_list, width=10)


for _ in range(10):
    smile(random.randint(50, 550), random.randint(50, 550))
sd.pause()
