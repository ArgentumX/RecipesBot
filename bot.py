import os, data

import keyboard as keyboard

from objects import Recipe, RecipesBase
import telebot
from telebot import types

bot = telebot.TeleBot('6856001156:AAFSstoCmTOvjUat-1UapdXN3b0PFAPDmr8')

recipe_base = RecipesBase(data.load_recipes())
current_recipe = 0

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_rand_recipe = types.KeyboardButton('Случайный рецепт')
    btn2 = types.KeyboardButton('Button_2')
    markup.add(btn_rand_recipe, btn2)
    send_message = 'Пожалуйста, выберите действие'
    bot.send_message(message.chat.id, send_message, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    global current_recipe
    if message.text == 'Случайный рецепт':
        board = types.InlineKeyboardMarkup()
        key_another_recipe = types.InlineKeyboardButton(text='Сопряжённый рецепт', callback_data='another_recipe')
        board.add(key_another_recipe)
        current_recipe = recipe_base.get_random_recipe()
        bot.send_message(message.chat.id, current_recipe.get_recipe_message(), reply_markup=board)
    elif message.text == 'Button_2':
        bot.send_message(message.chat.id, 'Вы выбрали button_2')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global current_recipe
    if call.data == 'another_recipe':
        current_recipe = recipe_base.get_recipe_by_id(current_recipe.conjugate_id)
        bot.send_message(call.message.chat.id, current_recipe.get_recipe_message())


bot.polling(none_stop=True)
