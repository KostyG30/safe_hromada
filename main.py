import telebot
from gevent.testing.travis import command
from telebot import types
from a_key import api
api = api
bot = telebot.TeleBot(api)
@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.from_user.id, f'Вас вітає чат-бот {chr(39)}{chr(39)}Безпечна громада{chr(39)}{chr(39)},'
                                           f'Тут ви можете написати звернення, скарги тощо')

bot.polling(non_stop=True, interval=0)