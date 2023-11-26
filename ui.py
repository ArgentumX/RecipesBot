from telebot import types


class ButtonMaster(object):
    def __init__(self, recipe_base, bot):
        self.recipe_base = recipe_base
        self.bot = bot
        self.current_recipe = 0

    def show_recipe(self, msg, recipe):
        if recipe is None:
            return
        board = types.InlineKeyboardMarkup()
        if recipe.conjugate_id != "":
            key_another_recipe = types.InlineKeyboardButton(text='Сопряжённый рецепт',
                                                            callback_data='another_recipe:' + recipe.conjugate_id)
            board.add(key_another_recipe)
        self.current_recipe = recipe
        self.bot.send_message(msg.chat.id, self.current_recipe.get_recipe_message(), reply_markup=board)

    def show_conjugated_recipe(self, msg, conjugated_id):
        if self.recipe_base.has_id(conjugated_id):
            self.show_recipe(msg, self.recipe_base.get_recipe_by_id(conjugated_id))

    def draw_start_menu(self, bot, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_rand_recipe = types.KeyboardButton('Случайный рецепт')
        btn_find_params = types.KeyboardButton('Поиск по параметрам')
        markup.add(btn_rand_recipe, btn_find_params)
        bot.send_message(msg.chat.id, 'Пожалуйста, выберите действие', reply_markup=markup)

    def draw_selection_search_menu(self, bot, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_find_cost = types.KeyboardButton('Поиск по цене')
        # btn_find_time = types.KeyboardButton('Поиск по времени')
        # btn_find_cook = types.KeyboardButton('Поиск по способу приготовления')
        btn_find_time_eat = types.KeyboardButton('Поиск по времени приёма пищи')
        btn_find_type = types.KeyboardButton('Поиск по типу блюда')
        markup.add(btn_find_cost, btn_find_time_eat, btn_find_type)
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

    def draw_cost(self, bot, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_400 = types.KeyboardButton('до 400 ₽')
        btn_400_700 = types.KeyboardButton('400 - 700 ₽')
        btn_700 = types.KeyboardButton('от 700 ₽')
        markup.add(btn_400, btn_400_700, btn_700)
        send_message = 'Выберите стоимость блюда'
        bot.send_message(msg.chat.id, send_message, reply_markup=markup)

    def draw_type(self, bot, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_des = types.KeyboardButton('Десерт')
        btn_base = types.KeyboardButton('Основное блюдо')
        btn_add = types.KeyboardButton('Закуска')
        markup.add(btn_des, btn_base, btn_add)
        send_message = 'Выберите тип блюда'
        bot.send_message(msg.chat.id, send_message, reply_markup=markup)
