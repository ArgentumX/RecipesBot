import os
from objects import Recipe


def load_recipes():
    result_recipes = []
    for file_name in os.listdir('recipes'):
        with open(os.path.join(os.getcwd() + "/recipes", file_name), 'r') as f:
            id = f.readline().strip()
            name = f.readline().strip()
            description = ""
            eatingtime = f.readline().strip()
            foodtype = f.readline().strip()
            cookingtime = f.readline().strip()
            coastfood = f.readline().strip()
            foodmass = f.readline().strip()
            for line in f.readlines():
                description += line

            rec = Recipe(id, name, description, eatingtime, foodtype, cookingtime, coastfood, foodmass)
            result_recipes.append(rec)
            f.close()
    print(f"Loaded {len(result_recipes)} recipes")
    return result_recipes
