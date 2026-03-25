import telebot
from telebot import types
from a_key import api
api = api
bot = telebot.TeleBot(api)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Звернення')
    but2 = types.KeyboardButton('Скарги')
    but3 = types.KeyboardButton('Пропозиції')
    markup.add(but1,but2,but3)
    bot.send_message(message.from_user.id, f'Вас вітає чат-бот {chr(39)}{chr(39)}Безпечна громада{chr(39)}{chr(39)},'
                                           f'Тут ви можете написати звернення, скарги тощо', reply_markup=markup)

bot.polling(non_stop=True, interval=0)