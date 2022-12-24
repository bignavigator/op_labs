import ingredients
import basic


class Burger(basic.Eat):
    res = "Вы съели бургер!"
    burger_recipe = {
        'Говядина': 10,
        'Говяжий жир': 2.5,
        'Луковица': 2,
        'Соль': 0.1,
        'Сливочное масло': 0.5
    }

    def e(self):
        self.energy = 0
        for i in ingredients.dict:
            if i in Burger.burger_recipe:
                self.energy += ingredients.dict[i][0]['energy'] * Burger.burger_recipe[i]
        return self.energy

    def c(self):
        self.cost = 0
        for i in ingredients.dict:
            if i in Burger.burger_recipe:
                self.cost += ingredients.dict[i][0]['cost'] * Burger.burger_recipe[i]
        return self.cost
