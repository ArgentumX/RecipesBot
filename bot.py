import os, data
from objects import Recipe, RecipesBase
import telebot
from telebot import types

bot = telebot.TeleBot('6856001156:AAFSstoCmTOvjUat-1UapdXN3b0PFAPDmr8')

recipe_base = RecipesBase(data.load_recipes())


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
    if message.text == 'Случайный рецепт':
        bot.send_message(message.chat.id, recipe_base.get_random_recipe().get_recipe_message())
        keyboard = types.InlineKeyboardMarkup()
        key_another_recipe = types.InlineKeyboardButton(text='Сопряжённый рецепт', callback_data='another_recipe')
        keyboard.add(key_another_recipe)
    elif message.text == 'Button_2':
        bot.send_message(message.chat.id, 'Вы выбрали button_2')


bot.polling(none_stop=True)
