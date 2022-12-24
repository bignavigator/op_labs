#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as a, room2 as b
from district.central_street.house2 import room1 as c, room2 as d
from district.soviet_street.house1 import room1 as e, room2 as f
from district.soviet_street.house2 import room1 as g, room2 as h


print('На районе живут: '+str(a.folks)+', '+str(b.folks)+', '+str(c.folks)+', '+str(d.folks)+', '+str(e.folks)+', '+str(f.folks)+', '+str(g.folks)+', '+str(h.folks))