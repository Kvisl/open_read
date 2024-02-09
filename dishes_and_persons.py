import json
from pprint import pprint

with open('dishes3.json', 'r') as f:
    cook_book = json.load(f)


def get_shop_list_by_dishes(dishes, person_count):
    recipes = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            recipes[name] = {
                'measure': measure,
                'quantity': recipes.get(name, {'quantity': 0})['quantity'] + quantity
            }

    return recipes


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4))

