import os, data

import keyboard as keyboard

from objects import Recipe, RecipesBase
import telebot
from telebot import types
from ui import ButtonMaster

bot = telebot.TeleBot('6856001156:AAFSstoCmTOvjUat-1UapdXN3b0PFAPDmr8')
recipe_base = RecipesBase(data.load_recipes())
UI = ButtonMaster(recipe_base, bot)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_rand_recipe = types.KeyboardButton('Случайный рецепт')
    btn_find_params = types.KeyboardButton('Поиск по параметрам')
    markup.add(btn_rand_recipe, btn_find_params)
    send_message = 'Пожалуйста, выберите действие'
    bot.send_message(message.chat.id, send_message, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Случайный рецепт':
        UI.recipe_display(1, message, 0)
    elif message.text == 'Поиск по параметрам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_find_cost = types.KeyboardButton('Поиск по цене')
        btn_find_time = types.KeyboardButton('Поиск по времени')
        btn_find_cook = types.KeyboardButton('Поиск по способу приготовления')
        btn_find_time_eat = types.KeyboardButton('Поиск по времени приёма пищи')
        btn_find_type = types.KeyboardButton('Поиск по типу блюда')
        markup.add(btn_find_cost, btn_find_time, btn_find_cook, btn_find_time_eat, btn_find_type)
        send_message = 'Выберите параметр поиска'
        bot.send_message(message.chat.id, send_message, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'another_recipe':
        UI.recipe_display(2, 0, call)


bot.polling(none_stop=True)
