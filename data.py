import os
from objects import Recipe


def load_recipes():
    result_recipes = []
    for file_name in os.listdir('recipes'):
        with open(os.path.join(os.getcwd() + "/recipes", file_name), 'r') as f:
            id = f.readline().strip()
            name = f.readline().strip()
            description = ""
            eating_time = f.readline().strip()
            food_type = f.readline().strip()
            cooking_time = f.readline().strip()
            cost = f.readline().strip()
            ingredients = f.readline().strip()
            for line in f.readlines():
                description += line

            rec = Recipe(id, name, eating_time, food_type, cooking_time, cost, ingredients, description)
            result_recipes.append(rec)
            f.close()
    print(f"Loaded {len(result_recipes)} recipes")
    return result_recipes
