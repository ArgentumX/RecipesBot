import os
from objects import Recipe


def load_recipes():
    result_recipes = []
    for file_name in os.listdir('recipes'):
        with open(os.path.join(os.getcwd() + "/recipes", file_name), 'r') as f:
            id = f.readline().strip()
            name = f.readline().strip()
            description = ""
            for line in f.readlines():
                description += line

            rec = Recipe(id, name, description)
            result_recipes.append(rec)
    print(f"Loaded {len(result_recipes)} recipes")
    return result_recipes
