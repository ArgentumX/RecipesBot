import os
from objects import Recipe, Ingredient


def load_recipes():
    result_recipes = []
    for file_name in os.listdir('recipes'):
        with open(os.path.join(os.getcwd() + "/recipes", file_name), 'r', encoding='utf-8') as f:
            id = f.readline().strip()
            name = f.readline().strip()
            eating_time = f.readline().strip()
            food_type = f.readline().strip()
            cooking_time = f.readline().strip()
            cost = f.readline().strip()
            ingredients = get_ingredient_list(f.readline().strip())
            cooking_method = f.readline().strip()
            conjugate_id = f.readline().strip()

            description = ""
            for line in f.readlines():
                description += line

            rec = Recipe(id, name, eating_time, food_type, cooking_time, cost, ingredients, cooking_method, conjugate_id, description)
            result_recipes.append(rec)
            f.close()
    print(f"Loaded {len(result_recipes)} recipes")
    return result_recipes


def get_ingredient_list(data_s):
    result = []
    for segment_s in data_s.split(", "):
        spited = segment_s.split(":")
        ingredient = Ingredient(spited[0], float(spited[1]), spited[2])
        result.append(Ingredient)
    return result