import random


class Recipe(object):
    def __init__(self, id, recipe_name, description):
        self.id = id
        self.recipes_name = recipe_name
        self.description = description


class RecipesBase(object):
    def __init__(self, recipes):
        self.recipes = recipes

    def get_recipe_by_id(self, id):
        for recipe in self.recipes:
            if recipe.id == id:
                return recipe

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.id == name:
                return recipe

    def get_recipes_amount(self):
        return len(self.recipes)

    def get_random_recipe(self):
        return self.recipes[random.randint(0, self.get_recipes_amount() - 1)]
