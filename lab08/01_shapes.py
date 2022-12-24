# -*- coding: utf-8 -*-

import simple_draw as sd
import time
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см results/exercise_01_shapes.jpg

# TODO здесь ваш код
start_point = sd.get_point(300, 350)

def hexagon(start_point, angle_hex, step):
    if step > 5:
        return
    hexagon1 = sd.get_vector(start_point=start_point, angle=angle_hex, length=50)
    hexagon1.draw()
    next_point = hexagon1.end_point
    next_angle = angle_hex - 60
    next_step = step + 1
    hexagon(start_point=next_point, angle_hex=next_angle, step=next_step)


hexagon(start_point=start_point, angle_hex=60, step=0)

time.sleep(1)
sd.clear_screen()

def triangle(start_point, angle_tri, step):
    if step > 2:
        return
    triangle1 = sd.get_vector(start_point=start_point, angle=angle_tri, length=50)
    triangle1.draw()
    next_point = triangle1.end_point
    next_angle = angle_tri - 120
    next_step = step + 1
    triangle(start_point=next_point, angle_tri=next_angle, step=next_step)


triangle(start_point=start_point, angle_tri=60, step=0)

time.sleep(1)
sd.clear_screen()

point_D = sd.get_point(350, 200)

sd.square(left_bottom=point_D, side=100, color=sd.COLOR_GREEN, width=1)
time.sleep(1)
sd.clear_screen()

def pentagon(start_point, angle_penta, step):
    if step > 4:
        return
    pentagon1 = sd.get_vector(start_point=start_point, angle=angle_penta, length=50)
    pentagon1.draw()
    next_point = pentagon1.end_point
    next_angle = angle_penta - 72
    next_step = step + 1
    pentagon(start_point=next_point, angle_penta=next_angle, step=next_step)


pentagon(start_point=start_point, angle_penta=72, step=0)

time.sleep(1)
sd.clear_screen()


sd.pause()
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
def figure(start_point, angle, step):
    while step < 6:
        hexagon = sd.get_vector(start_point=start_point, angle=angle, length=50)
        hexagon.draw()
        next_point = hexagon.end_point
        next_angle = angle - 60
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)
        return
    while 5 < step < 11:
        pentagon = sd.get_vector(start_point=start_point, angle=angle, length=50)
        pentagon.draw()
        next_point = pentagon.end_point
        next_angle = angle - 72
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)
        return
    while 10 < step < 13:
        triangle = sd.get_vector(start_point=start_point, angle=angle, length=50)
        triangle.draw()
        next_point = triangle.end_point
        next_angle = angle - 120
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)
        return
    while 12 < step < 17:
        square = sd.get_vector(start_point=start_point, angle=angle, length=50)
        square.draw()
        next_point = square.end_point
        next_angle = angle - 90
        next_step = step + 1
        figure(start_point=next_point, angle=next_angle, step=next_step)

figure(start_point=start_point, angle=180, step=0)

time.sleep(3)
sd.clear_screen()