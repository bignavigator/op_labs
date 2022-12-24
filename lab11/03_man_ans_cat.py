# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код


class RIP(Exception):
    """Исключение если кто то умер от голода."""


class BUM(Exception):
    """Исключение если кто то стал бомжом."""


class Animal:
    """Родительский класс для всех животных."""
    _name = None
    _fullness = 100
    _food = 0

    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f"Деньги: {self.money}\nСытость человека: {self.fullness}"

    @property
    def name(self) -> str:
        """Имя. Имя даётся раз и навсегда!"""
        return self._name

    @property
    def fullness(self) -> int:
        """Методы получения сытости."""
        return self._fullness

    @fullness.setter
    def fullness(self, fullness: int):
        """Метод установки значения сытости. Если сытость меньше нуля,
        то будет вызвано исключение RIP. Максимальное значение 100."""
        if fullness < 0: raise RIP(f"{self} - fullness < 0!")
        self._fullness = fullness if fullness < 100 else 100

    @property
    def food(self) -> int:
        """Методы получения сытости."""
        return self._food

    @food.setter
    def food(self, food: int):
        """Метод установки значения сытости. Если сытость меньше нуля,
        то будет вызвано исключение RIP. Максимальное значение 100."""
        if food < 0: raise RIP(f"{self} - food < 0!")
        self._food = food

    def sleep(self):
        self._fullness -= 10


class Cat(Animal):
    _human = None

    def __str__(self) -> str:
        return f"Сытость кота: {self.fullness}"

    @property
    def human(self):
        """Ссылка на хозяина."""
        return self._human

    @human.setter
    def human(self, human: "Human"):
        """Метод изменение хозяина."""
        self._human = human

    @property
    def house(self):
        """Ссылка на хату."""
        if not self._human: return None
        return self._human.house

    def act(self, house):
        self.sleep()
        if (self.food >= 10) and (self.fullness < 80):
            self.food -= 10
            self.fullness += 20
        if randint(1, 100) > 50:
            house.dirt += 5
            self.fullness -= 10


class Human(Animal):
    _cat = None
    _money = 400

    @property
    def cat(self):
        """Ссылка на кота."""
        return self._cat

    @cat.setter
    def cat(self, cat: "Cat"):
        """Метод установки кота."""
        self._cat = cat
        self._cat.human = self

    @property
    def money(self) -> int:
        """Метод получения количества кеша."""
        return self._money

    @money.setter
    def money(self, money: int):
        """Метод установки количества кеша. Если кеш меньше нуля,
        то будет вызвано исключение BUM."""
        if money < 0: raise BUM(f"{self} - money < 0!")
        self._money = money

    @property
    def house(self):
        """Ссылка на хату."""
        return self._house

    @house.setter
    def house(self, house: "House"):
        """Метод изменение хаты."""
        self._house = house

    def act(self, cat, house):
        self.sleep()
        if (cat.fullness < 40) and (self.money >= 130):
            self.money -= 130
            cat.food += 80
            self.food += 55
        if (self.food >= 10) and (self.fullness < 80):
            self.food -= 10
            self.fullness += 20
        if house.dirt >= 100:
            house.dirt -= 100
            self.fullness -= 20
        if day % 30 == 0:
            self.money += 400


class House:
    _name = None
    _dirt = 0

    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f"Загрязнённость дома: {self._dirt}"

    @property
    def name(self) -> str:
        """Имя. Которое можно изменять!"""
        return self._name

    @name.setter
    def name(self, name: str):
        """Метод смены имени, т.к. своё убежище
        ты можешь называть как тебе угодно."""
        self._name = name

    @property
    def dirt(self) -> int:
        """Имя. Которое можно изменять!"""
        return self._dirt

    @dirt.setter
    def dirt(self, dirt: int):
        """Метод смены имени, т.к. своё убежище
        ты можешь называть как тебе угодно."""
        self._dirt = dirt


Timosha = Cat("Timosha")
Lionia = Cat("Lionia")
Pavelko = Human("Pavelko")

Jugansk_House = House("Jugansk house")

# Павелко берёт кота, на улице
Pavelko.cat = Timosha
Pavelko.cat = Lionia
# Дальше он приносит его в свою квартиру
Pavelko.house = Jugansk_House

print(f"{Timosha}, хозяин - {Timosha.human}, хата - {Timosha.house}")
# Cat(name=Timosha), хозяин - Human(name=Pavelko), хата - House(name=Little house)

for day in range(1, 366):
    Pavelko.act(Timosha, Jugansk_House)
    Timosha.act(Jugansk_House)
    Lionia.act(Jugansk_House)
    print('================= day {} ================'.format(day))
    print(Pavelko)
    print(Timosha)
    print(Lionia)
    print(Jugansk_House)

# Cat(name=Timosha), хозяин - Human(name=Pavelko), хата - House(name=Big house)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
