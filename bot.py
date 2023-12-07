import os, data

from objects import Recipe, RecipesBase
import telebot
from telebot import types
from ui import ButtonMaster

bot = telebot.TeleBot('6856001156:AAFSstoCmTOvjUat-1UapdXN3b0PFAPDmr8')
recipe_base = RecipesBase(data.load_recipes())
UI = ButtonMaster(recipe_base, bot)


@bot.message_handler(commands=['start'])
def start(message):

    UI.draw_start_menu(bot, message)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Случайный рецепт':
        UI.show_recipe(message, recipe_base.get_random_recipe())
    elif message.text == 'Поиск по параметрам':
        UI.draw_selection_search_menu(bot, message)
    elif message.text == 'Поиск по времени приёма пищи':
        UI.draw_eating_time(bot, message)
    elif message.text == 'Обед':
        UI.show_recipe(message, recipe_base.get_recipe_by_eating_time("обед"))
        UI.draw_start_menu(bot, message)
    elif message.text == 'Завтрак':
        UI.show_recipe(message, recipe_base.get_recipe_by_eating_time("завтрак"))
        UI.draw_start_menu(bot, message)
    elif message.text == 'Ужин':
        UI.show_recipe(message, recipe_base.get_recipe_by_eating_time("ужин"))
        UI.draw_start_menu(bot, message)
    elif message.text == 'Поиск по цене':
        UI.draw_cost(bot, message)
    elif message.text == 'до 200 ₽':
        UI.show_recipe(message, recipe_base.get_recipe_by_cost_interval(0, 200))
        UI.draw_start_menu(bot, message)
    elif message.text == '200 - 400 ₽':
        UI.show_recipe(message, recipe_base.get_recipe_by_cost_interval(200, 400))
        UI.draw_start_menu(bot, message)
    elif message.text == 'от 400 ₽':
        UI.show_recipe(message, recipe_base.get_recipe_by_cost_interval(400, 1000000000))
        UI.draw_start_menu(bot, message)
    elif message.text == 'Поиск по типу блюда':
        UI.draw_type(bot, message)
    elif message.text == 'Десерт':
        UI.show_recipe(message, recipe_base.get_recipe_by_food_type('десерт'))
        UI.draw_start_menu(bot, message)
    elif message.text == 'Основное блюдо':
        UI.show_recipe(message, recipe_base.get_recipe_by_food_type('основное'))
        UI.draw_start_menu(bot, message)
    elif message.text == 'Закуска':
        UI.show_recipe(message, recipe_base.get_recipe_by_food_type('закуска'))
        UI.draw_start_menu(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    spited = call.data.split(":")
    if spited[0] == 'another_recipe':
        UI.show_conjugated_recipe(call.message, spited[1])


bot.polling(none_stop=True)
