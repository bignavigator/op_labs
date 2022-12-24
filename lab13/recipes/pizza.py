import ingredients
import basic


class Pizza(basic.Eat):
    res = "Вы съели пиццу!"
    pizza_recipe = {
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

    def e(self):
        self.energy = 0
        for i in ingredients.dict:
            if i in Pizza.pizza_recipe:
                self.energy += ingredients.dict[i][0]['energy'] * Pizza.pizza_recipe[i]
        return self.energy

    def c(self):
        self.cost = 0
        for i in ingredients.dict:
            if i in Pizza.pizza_recipe:
                self.cost += ingredients.dict[i][0]['cost'] * Pizza.pizza_recipe[i]
        return self.cost
