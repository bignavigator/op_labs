# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg

# TODO здесь ваш код
print("Enter number for color:"
      "1 = red, 2 = orange, 3 = yellow, 4 = green, 5 = cyan, 6 = blue, 7 = purple")
user_color = input()

match user_color:
    case '1': user_color = sd.COLOR_RED
    case '2': user_color = sd.COLOR_ORANGE
    case '3': user_color = sd.COLOR_YELLOW
    case '4': user_color = sd.COLOR_GREEN
    case '5': user_color = sd.COLOR_CYAN
    case '6': user_color = sd.COLOR_BLUE
    case '7': user_color = sd.COLOR_PURPLE

start_point = sd.get_point(300, 350)
def hexagon(start_point, angle_hex, step):
    if step > 5:
        return
    hexagon1 = sd.get_vector(start_point=start_point, angle=angle_hex, length=50)
    hexagon1.draw(color=user_color)
    next_point = hexagon1.end_point
    next_angle = angle_hex - 60
    next_step = step + 1
    hexagon(start_point=next_point, angle_hex=next_angle, step=next_step)


hexagon(start_point=start_point, angle_hex=60, step=0)

sd.sleep(1)
sd.clear_screen()

def triangle(start_point, angle_tri, step):
    if step > 2:
        return
    triangle1 = sd.get_vector(start_point=start_point, angle=angle_tri, length=50)
    triangle1.draw(color=user_color)
    next_point = triangle1.end_point
    next_angle = angle_tri - 120
    next_step = step + 1
    triangle(start_point=next_point, angle_tri=next_angle, step=next_step)


triangle(start_point=start_point, angle_tri=60, step=0)
sd.sleep(1)
sd.clear_screen()

point_D = sd.get_point(350, 200)

sd.square(left_bottom=point_D, side=100, color=user_color, width=1)
sd.sleep(1)
sd.clear_screen()

def pentagon(start_point, angle_penta, step):
    if step > 4:
        return
    pentagon1 = sd.get_vector(start_point=start_point, angle=angle_penta, length=50)
    pentagon1.draw(color=user_color)
    next_point = pentagon1.end_point
    next_angle = angle_penta - 72
    next_step = step + 1
    pentagon(start_point=next_point, angle_penta=next_angle, step=next_step)


pentagon(start_point=start_point, angle_penta=72, step=0)

sd.sleep(1)
sd.clear_screen()


sd.pause()

def figure(start_point, angle, step):
    while step < 6:
        hexagon = sd.get_vector(start_point=start_point, angle=angle, length=50)
        hexagon.draw(color=user_color)
        next_point = hexagon.end_point
        next_angle = angle - 60
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)
        return
    while 5 < step < 11:
        pentagon = sd.get_vector(start_point=start_point, angle=angle, length=50)
        pentagon.draw(color=user_color)
        next_point = pentagon.end_point
        next_angle = angle - 72
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)
        return
    while 10 < step < 13:
        triangle = sd.get_vector(start_point=start_point, angle=angle, length=50)
        triangle.draw(color=user_color)
        next_point = triangle.end_point
        next_angle = angle - 120
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)
        return
    while 12 < step < 17:
        square = sd.get_vector(start_point=start_point, angle=angle, length=50)
        square.draw(color=user_color)
        next_point = square.end_point
        next_angle = angle - 90
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)

figure(start_point=start_point, angle=180, step=0)

sd.sleep(3)
sd.clear_screen()
