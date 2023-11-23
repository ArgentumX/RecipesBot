from telebot import types


class ButtonMaster(object):
    def __init__(self, recipe_base, bot):
        self.recipe_base = recipe_base
        self.bot = bot
        self.current_recipe = 0

    def show_recipe(self, msg, recipe):
        board = types.InlineKeyboardMarkup()
        if recipe.conjugate_id != "":
            key_another_recipe = types.InlineKeyboardButton(text='Сопряжённый рецепт', callback_data='another_recipe:' + recipe.conjugate_id)
            board.add(key_another_recipe)
        self.current_recipe = recipe
        self.bot.send_message(msg.chat.id, self.current_recipe.get_recipe_message(), reply_markup=board)

    def show_conjugated_recipe(self, conjugated_id):
        if self.recipe_base.has_id(conjugated_id):
            self.show_recipe(msg, self.recipe_base.get_recipe_by_id(conjugated_id))

    def draw_start_menu(self, bot, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_rand_recipe = types.KeyboardButton('Случайный рецепт')
        btn_find_params = types.KeyboardButton('Поиск по параметрам')
        markup.add(btn_rand_recipe, btn_find_params)
        send_message = 'Пожалуйста, выберите действие'
        bot.send_message(msg.chat.id, send_message, reply_markup=markup)

    def draw_selection_search_menu(self, bot, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_find_cost = types.KeyboardButton('Поиск по цене')
        btn_find_time = types.KeyboardButton('Поиск по времени')
        btn_find_cook = types.KeyboardButton('Поиск по способу приготовления')
        btn_find_time_eat = types.KeyboardButton('Поиск по времени приёма пищи')
        btn_find_type = types.KeyboardButton('Поиск по типу блюда')
        markup.add(btn_find_cost, btn_find_time, btn_find_cook, btn_find_time_eat, btn_find_type)
        send_message = 'Выберите параметр поиска'
        bot.send_message(msg.chat.id, send_message, reply_markup=markup)

    def draw_eating_time(self, bot, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_br = types.KeyboardButton('Завтрак')
        btn_lun = types.KeyboardButton('Обед')
        btn_din = types.KeyboardButton('Ужин')
        markup.add(btn_br, btn_lun, btn_din)
        send_message = 'Выберите время приёма пищи'
        bot.send_message(msg.chat.id, send_message, reply_markup=markup)
