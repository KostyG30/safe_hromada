import telebot
from gevent.testing.travis import command
from telebot import types
from a_key import api
api = api
bot = telebot.TeleBot(api)
@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Даскаво просимо")