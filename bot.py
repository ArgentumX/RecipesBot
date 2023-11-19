import os, data
from objects import Recipe, RecipesBase
import telebot
from telebot import types

bot = telebot.TeleBot('6856001156:AAFSstoCmTOvjUat-1UapdXN3b0PFAPDmr8')

recipe_base = RecipesBase(data.load_recipes())


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Случайный рецепт')
    btn2 = types.KeyboardButton('Button_2')
    markup.add(btn1, btn2)
    send_message = 'Пожалуйста, выберите действие'
    bot.send_message(message.chat.id, send_message, reply_markup=markup)

    markup.add(btn1)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Случайный рецепт':
        bot.send_message(message.chat.id, 'Вы выбрали случайный рецепт')
    elif message.text == 'Button_2':
        bot.send_message(message.chat.id, 'Вы выбрали button_2')
