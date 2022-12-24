import ingredients

res = "Вы съели бургер!"
recipe = {
    'Говядина': 10,
    'Говяжий жир': 2.5,
    'Луковица': 2,
    'Соль': 0.1,
    'Сливочное масло': 0.5
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