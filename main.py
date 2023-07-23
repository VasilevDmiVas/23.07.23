import datetime
import telebot
import requests
from telebot import types
import json
API_TOKEN = '6101280193:AAF8o3dtvIEXe5onAh5LGKGh1PVBoC_khjhg'
API_Weather = 'fc754d58a718cae8f03a6c3a798418ff'
bot = telebot.TeleBot(API_TOKEN)
time1 = datetime.datetime.now()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '''Привет всем данный бот выполняет следующее
     при вводе команды вида /date - выводит сегодняшнюю дату
    при вводе команды вида /time - выводит теперешнее время
    при наборе города выводит температуру воздуха в нем''')

@bot.message_handler(commands=['date'])
def send_date(message):
    date_now = time1.strftime('%Y.%m.%d')
    bot.reply_to(message, f'Сегодняшний день {date_now}')

@bot.message_handler(commands=['time'])
def send_time(message):
    time_now = time1.strftime('%H:%M:%S')
    bot.reply_to(message, f'Время сейчас = {time_now}')

@bot.message_handler(content_types=['text'])
def get_wether(message):
    city = message.text.strip().lower()
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Weather}&units=metric')
    if result.status_code == 200:
        data = json.loads(result.text)
        bot.reply_to(message, f'Сейчас погода в {city}е {data["main"]["temp"]} С')
    else:
        bot.reply_to(message, f'Город указан не верно')

# @bot.message_handler(content_types=['text'])
# def send_welcome(message):
#     markup = types.InlineKeyboardMarkup
#     btn1 = types.InlineKeyboardButton('День недели', callback_data='d')
#     markup.add(btn1)
#     bot.send_message(message.chat.id, 'Выбер', reply_markup=markup)

bot.infinity_polling()

# content_types - любой текст команада