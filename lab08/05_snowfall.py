# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflakes = {}
for i in range(N):
    snowflakes[i] = {}
    snowflakes[i]['x'] = sd.random_number(i * 30, (i + 1) * 30 - 30)
    snowflakes[i]['y'] = 700
    snowflakes[i]['length'] = sd.random_number(5, 15)
    snowflakes[i]['factor_a'] = sd.random_number(1, 8)/10
    snowflakes[i]['factor_b'] = sd.random_number(1, 8)/10
    snowflakes[i]['factor_c'] = sd.random_number(30, 60)
    snowflakes[i]['speed'] = sd.random_number(20, 30)

flag_of_stop = False

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

while True:
    for i, snowflake_item in snowflakes.items():
        point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
        sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'],
                     color=sd.background_color)
        snowflake_item['y'] -= snowflake_item['speed']
        snowflake_item['x'] += sd.random_number(-15, 15)
        point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
        sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])
        if snowflake_item['y'] < 10:
            sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                         factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])
            snowflake_item['y'] = 700
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()