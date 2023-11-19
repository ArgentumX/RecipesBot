import os, data

import keyboard as keyboard

from objects import Recipe, RecipesBase
import telebot
from telebot import types

bot = telebot.TeleBot('6856001156:AAFSstoCmTOvjUat-1UapdXN3b0PFAPDmr8')

recipe_base = RecipesBase(data.load_recipes())
current_recipe = 0


def recipe_display(todo, msg, call, cur_rec):
    board = types.InlineKeyboardMarkup()
    key_another_recipe = types.InlineKeyboardButton(text='Сопряжённый рецепт', callback_data='another_recipe')
    board.add(key_another_recipe)
    global c_r
    if todo == 1:
        c_r = recipe_base.get_random_recipe()
        return bot.send_message(msg.chat.id, c_r.get_recipe_message(), reply_markup=board)
    elif todo == 2:
        c_r = recipe_base.get_recipe_by_id(c_r.conjugate_id)
        return bot.send_message(call.message.chat.id, c_r.get_recipe_message(), reply_markup=board)


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
    global current_recipe
    if message.text == 'Случайный рецепт':
        recipe_display(1, message, 0, 0)
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
    global current_recipe
    if call.data == 'another_recipe':
        recipe_display(2, 0, call, current_recipe)


bot.polling(none_stop=True)
