#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

film1 = (my_favorite_movies[0:10])
film2 = (my_favorite_movies[12:25])
film3 = (my_favorite_movies[27:33])
film4 = (my_favorite_movies[35:40])
film5 = (my_favorite_movies[42:57])

my_list = [film1, film2, film3, film4, film5]



