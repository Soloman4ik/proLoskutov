#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_london = ((moscow[0]-london[0])**2+(moscow[1]-london[1]))**.5
moscow_paris = ((moscow[0]-paris[0])**2+(moscow[1]-paris[1]))**.5
london_paris=((london[0]-paris[0])**2+(london[1]-paris[1])**2)**.5

distance = dict()

distance ['Moscow'] = {}
distance ['Moscow']['London'] = moscow_london
distance ['Moscow']['Paris'] = moscow_paris

distance ['London'] = {}
distance ['London']['Moscow'] = moscow_london
distance ['London']['Paris'] = london_paris

distance ['Paris'] = {}
distance ['Paris']['London'] = moscow_paris
distance ['Paris']['London'] = london_paris

pprint(distance)







