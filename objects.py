import random


class Recipe(object):
    def __init__(self, id, recipe_name, eating_time, food_type, cooking_time, cost, ingredients, description):
        self.id = id
        self.recipes_name = recipe_name
        self.eating_time = eating_time
        self.food_type = food_type
        self.cooking_time = cooking_time
        self.cost = cost
        self.ingredients = ingredients
        self.description = description

    def get_recipe_message(self):
        result = ""
        result += self.recipes_name + f"({self.food_type})\n\n"
        result += f"Время готовки: {self.cooking_time} минут\n"
        result += f"Цена: {self.cost} рублей\n\n"

        result += self.description
        return result


class RecipesBase(object):
    def __init__(self, recipes):
        self.recipes = recipes

    def get_recipe_by_id(self, id):
        for recipe in self.recipes:
            if recipe.id == id:
                return recipe

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe

    def get_recipes_amount(self):
        return len(self.recipes)

    def get_random_recipe(self):
        return self.recipes[random.randint(0, self.get_recipes_amount() - 1)]
