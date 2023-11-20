import random


class Recipe(object):
    def __init__(self, id, recipe_name, eating_time, food_type, cooking_time, cost, ingredients, cooking_method,conjugate_id, description):
        self.id = id
        self.recipes_name = recipe_name
        self.eating_time = eating_time
        self.food_type = food_type
        self.cooking_time = cooking_time
        self.cost = cost
        self.ingredients = ingredients
        self.cooking_method = cooking_method
        self.conjugate_id = conjugate_id
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
        print("not found")

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe

    def get_recipes_amount(self):
        return len(self.recipes)

    def get_random_recipe(self):
        return self.recipes[random.randint(0, self.get_recipes_amount() - 1)]

    def get_recipes_below_cost(self, cost):
        result = []
        for recipe in self.recipes:
            if recipe.cost <= cost:
                result.append(recipe)
        return result

    def get_recipes_below_time(self, time):
        result = []
        for recipe in self.recipes:
            if recipe.time <= time:
                result.append(recipe)
        return result

    def get_recipes_by_method(self, method):
        result = []
        for recipe in self.recipes:
            if recipe.cooking_method == method:
                result.append(recipe)
        return result

    def get_recipes_by_eating_time(self, eating_time):
        result = []
        for recipe in self.recipes:
            if recipe.eating_time == eating_time:
                result.append(recipe)
        return result

    def get_recipes_by_food_type(self, food_type):
        result = []
        for recipe in self.recipes:
            if recipe.food_type == food_type:
                result.append(recipe)
        return result




