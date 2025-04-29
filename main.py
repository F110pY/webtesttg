import telebot
from telebot import types
from telebot.types import WebAppInfo

bot = telebot.TeleBot('7698724074:AAFsRqm-FP5B0vul9xYsmBzJ2Ap7wae7HsE')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton('Hello', web_app=WebAppInfo(url='https://f110py.github.io/webtesttg/'))
    markup.add(button)
    bot.send_message(message.chat.id, 'Hello', reply_markup=markup)


@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    bot.send_message(message.chat.id, message.web_app_data.data)


bot.polling(none_stop=True)