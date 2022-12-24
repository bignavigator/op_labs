#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time

import simple_draw as sd

sd.resolution = (1200, 600)

def draw_buble(position, radius=50, step = 5, color=sd.COLOR_GREEN, width=1):
    for y in range(3):
        sd.circle(center_position=position, radius=radius, color=color, width=width)
        radius += step
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код


buble_position = sd.get_point(300, 300)
draw_buble(position=buble_position, radius=50)

time.sleep(1)
sd.clear_screen()
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код
buble_position = sd.get_point(600, 300)
draw_buble(position=buble_position, radius=70, step=10, color=sd.COLOR_RED, width=2)

time.sleep(1)
sd.clear_screen()
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range(100, 1001, 100):
    buble_position = sd.get_point(x, 500)
    draw_buble(position=buble_position, radius=30, color=sd.COLOR_YELLOW)

time.sleep(1)
sd.clear_screen()
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        buble_position = sd.get_point(x, y)
        draw_buble(position=buble_position, radius=30, color=sd.COLOR_WHITE)

time.sleep(1)
sd.clear_screen()
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
sd.resolution = (330, 600)
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    radius = random.randint(10, 40)
    color = sd.random_color()
    draw_buble(position=point, color=color, radius=radius)


sd.pause()
