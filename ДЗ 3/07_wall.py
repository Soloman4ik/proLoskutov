# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.background_color = 210, 105, 30
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
sd.resolution = (600, 600)
size_x = 100
size_y = 50
number = 0
kladka = 0
for y in range(0, sd.resolution[1], size_y):
    kladka += 1
    for x in range(0, sd.resolution[0], size_x):
        if kladka % 2 == 0:
            sd.rectangle(left_bottom=sd.get_point(x, y), right_top=sd.get_point(x+size_x, y+size_y), color=(0, 0, 0),
                     width=3)
        else:
            sd.rectangle(left_bottom=sd.get_point(x+size_x/2, y), right_top=sd.get_point(x + size_x + size_x/2, y + size_y),
                         color=(0, 0, 0), width=3)




sd.pause()
