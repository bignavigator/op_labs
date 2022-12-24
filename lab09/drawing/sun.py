#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# TODO здесь ваш код
sd.resolution = (1300, 750)
SUN_SIZE = 100
SUN_COLOR = sd.COLOR_YELLOW


def draw_sun(x, y, color):

    # рисуем лицо
    face_point = sd.get_point(x=x, y=y)
    sd.circle(center_position=face_point, radius=SUN_SIZE, color=color, width=0)


# рисуем смайлы
for _ in range(1):
    rnd_point = sd.get_point(1200, 600)
    draw_sun(rnd_point.x, rnd_point.y, SUN_COLOR)

sd.pause()
