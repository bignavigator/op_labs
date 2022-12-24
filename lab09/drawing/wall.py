#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич
# размер кирпича
x = 40
y = 20

half_brick = x // 2

brick_x_count = sd.resolution[0] // x
brick_y_count = sd.resolution[1] // y

start_x = 0
start_y = 200
end_x = start_x + x
end_y = start_y + y
sd.resolution = (1300, 750)

for brick_y in range(8):

    # определяем кол-во кирпичей в ряду
    if brick_y % 2 == 1:
        x_count += 1
    else:
        x_count = brick_x_count

    for brick_x in range(9):

        if brick_y % 2 == 1:
            if brick_x == 0:
                start_position = sd.get_point(start_x, start_y)
                end_position = sd.get_point(end_x-half_brick, end_y)
            elif brick_x == x_count-1:
                start_position = sd.get_point(start_x-half_brick, start_y)
                end_position = sd.get_point(end_x-x, end_y)
            else:
                start_position = sd.get_point(start_x-half_brick, start_y)
                end_position = sd.get_point(end_x-half_brick, end_y)
        else:
            start_position = sd.get_point(start_x, start_y)
            end_position = sd.get_point(end_x, end_y)

        sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_BLACK, width=1)

        # двигаем кирпич по x
        start_x += x
        end_x += x

        sd.sleep(0.03)

    # возвращаем по х в исходное положение
    start_x = 0
    end_x = x

    # двигаем кирпич по y
    start_y = end_y
    end_y += y

start_point = sd.get_point(0, 360)
second_point = sd.get_point(360, 360)
end_point = sd.get_point(180, 420)
ROOF_COLOR = sd.COLOR_DARK_PURPLE

def triangle(start_point, second_point, end_point):
    sd.line(start_point=start_point, end_point=second_point, color=sd.COLOR_DARK_PURPLE)
    sd.line(start_point=second_point, end_point=end_point, color=sd.COLOR_DARK_PURPLE)
    sd.line(start_point=end_point, end_point=start_point, color=sd.COLOR_DARK_PURPLE)


triangle(start_point=start_point, second_point=second_point, end_point=end_point)

sd.pause()
