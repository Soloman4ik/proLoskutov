# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
start_x = 50
start_y = 50
end_x = 450
end_y = 550
# for color in rainbow_colors:
#     sd.line(start_point=sd.get_point(start_x, start_y), end_point=sd.get_point(end_x, end_y),
#             color=color, width=4)
#     step = 5
#     start_x += step
#     end_x += step

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваp
sd.resolution(600, 600)
point = sd.get_point(sd.resolution[0]/2, -280)
step = 10
radius = 300
for color in rainbow_colors:
    sd.circle(center_position=point, radius=radius, color=color, width=step)
    radius = radius + step

sd.pause()
