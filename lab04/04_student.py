#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
i = 0
academic_year_expenses = 0
academic_year_grants = educational_grant * 10
while i < 10:
    i += 1
    academic_year_expenses += expenses
    expenses *= 1.03
money_asking = academic_year_expenses - academic_year_grants
print(money_asking)