import ingredients

res = "Вы съели вок!"
recipe = {
    'Креветка очищенная': 4,
    'Фунчоза': 2.5,
    'Корень имбиря': 0.5,
    'Капуста китайская': 5,
    'Лайм': 0.5,
    'Перец рамиро': 1.5,
    'Соевый соус': 0.25,
    'Кунжутное масло': 0.05,
    'Красный лук': 0.5,
    'Растительное масло': 0.4,
    'Чеснок': 0.05,
    'Кинза': 1.5,
    'Морковь': 0.5,
    'Сахар': 0.05,
    'Кунжутное семечко': 0.05
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