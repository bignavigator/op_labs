import ingredients
import basic


class Wok(basic.Eat):
    res = "Вы съели вок!"
    wok_recipe = {
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

    def e(self):
        self.energy = 0
        for i in ingredients.dict:
            if i in Wok.wok_recipe:
                self.energy += ingredients.dict[i][0]['energy'] * Wok.wok_recipe[i]
        return self.energy

    def c(self):
        self.cost = 0
        for i in ingredients.dict:
            if i in Wok.wok_recipe:
                self.cost += ingredients.dict[i][0]['cost'] * Wok.wok_recipe[i]
        return self.cost
