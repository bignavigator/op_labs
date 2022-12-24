# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
user_color = sd.COLOR_PURPLE

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

sd.sleep(1)
sd.clear_screen()

point_D = sd.get_point(350, 200)


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

print("Enter number for figure:"
      "1 = triangle, 2 = square, 3 = pentagon, 4 = hexagon")
user_figure = input()
match user_figure:
    case '1': triangle(start_point=start_point, angle_tri=60, step=0)
    case '2': sd.square(left_bottom=point_D, side=100, color=user_color, width=1)
    case '3': pentagon(start_point=start_point, angle_penta=72, step=0)
    case '4': hexagon(start_point=start_point, angle_hex=60, step=0)

sd.sleep(1)
sd.clear_screen()


sd.pause()
