import ingredients

res = "Вы съели пиццу!"
recipe = {
    'Кипячёная вода': 2,
    'Мука': 1.25,
    'Дрожжи': 0.1,
    'Соль': 0.1,
    'Сахар': 0.2,
    'Оливковое масло': 0.2,
    'Сливочное масло': 0.5,
    'Чеснок': 0.02,
    'Сыр': 2.5,
    'Пармезан': 1
}


def e():
    energy = 0
    for i in ingredients.dict:
          if i in recipe:
                energy += ingredients.dict[i][0]['energy']*recipe[i]
    return energy


def c():
    cost = 0
    for i in ingredients.dict:
          if i in recipe:
                cost += ingredients.dict[i][0]['cost']*recipe[i]
    return cost


energy = e()
cost = c()
print(cost)