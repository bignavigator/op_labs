#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингридиентов - создать соответствующие функции в модуле my_burger
import my_burger

print(my_burger.bun())
print(my_burger.cutlet())
print(my_burger.cucumber())
print(my_burger.tomato())
print(my_burger.mayonnaise())
print(my_burger.cheese())

print("Рецепт чизбургера:")
print(my_burger.oil())
print(my_burger.onion())
print(my_burger.mayonnaise())
print(my_burger.ketchup())
print(my_burger.cucumber())
print(my_burger.vinegar())
print(my_burger.stuffing())
print(my_burger.bun())
print(my_burger.cucumber())
print(my_burger.tomato())
print(my_burger.salad())
print(my_burger.mustard())