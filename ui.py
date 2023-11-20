from telebot import types


class ButtonMaster(object):
    def __init__(self, recipe_base, bot):
        self.recipe_base = recipe_base
        self.bot = bot
        self.current_recipe = 0

    def recipe_display(self, todo, msg, call):
        board = types.InlineKeyboardMarkup()
        key_another_recipe = types.InlineKeyboardButton(text='Сопряжённый рецепт', callback_data='another_recipe')
        board.add(key_another_recipe)
        if todo == 1:
            self.current_recipe = self.recipe_base.get_random_recipe()
            return self.bot.send_message(msg.chat.id, self.current_recipe.get_recipe_message(), reply_markup=board)
        elif todo == 2:
            self.current_recipe = self.recipe_base.get_recipe_by_id(self.current_recipe.conjugate_id)
            return self.bot.send_message(call.message.chat.id, self.current_recipe.get_recipe_message(), reply_markup=board)
