from telebot import types


class ButtonMaster(object):
    def __init__(self, recipe_base, bot):
        self.recipe_base = recipe_base
        self.bot = bot
        self.current_recipe = 0

    def show_recipe(self, msg, recipe):
        board = types.InlineKeyboardMarkup()
        key_another_recipe = types.InlineKeyboardButton(text='Сопряжённый рецепт', callback_data='another_recipe')
        board.add(key_another_recipe)
        self.current_recipe = recipe
        self.bot.send_message(msg.chat.id, self.current_recipe.get_recipe_message(), reply_markup=board)

    def show_conjugated_recipe(self, msg):
        self.show_recipe(msg, self.recipe_base.get_recipe_by_id(self.current_recipe.conjugate_id))

    def draw_start_menu(self):
        # Отрисовка стартового меню (Таня)
        pass