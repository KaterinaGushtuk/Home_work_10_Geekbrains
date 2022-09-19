import telebot
from datetime import datetime as dt
import os
from os.path import exists
import Main_bot as Mb
from PIL import Image
from urllib.request import urlopen

bot = telebot.TeleBot('5472166248:AAFWdydepwkbkxYNKYPfgeGmcczi0C_h7Zo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,'<b>Привет, красавчик</b>', parse_mode ='html')



@bot.message_handler(commands=['hello'])
def hello_message(message):
    bot.reply_to(message,f'<b>{message.from_user.first_name}, хочешь что-то спросить? Выполни команду help</b>', parse_mode ='html')


@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = 'Для проведения расчетов введите ОДНОСЛОЖНОЕ выражение в следующем формате\n'\
                'calc#<первое число> <оператор> <второе число>\n'\
                'При вводе выражения в неверном формате (введено более одного оператора; вместо чисел введены буквы и т.д.) программа выдаст ошибку\n'\
                'Для просмотра логов требуется выполнить операцию /log'
    bot.reply_to(message,f'Справка по работе калькулятора:\n{help_text}')


@bot.message_handler(commands=['bye'])
def bye_message(message):
    photo = Image.open(urlopen('https://krasivosti.pro/uploads/posts/2021-04/1617963834_45-p-spyashchie-koti-smeshnie-52.jpg'))
    bot.send_photo(message.from_user.id, photo)
    bot.reply_to(message, f'<b>Сладких снов {message.from_user.first_name} {message.from_user.last_name}. Текущее время: {dt.now()}</b>', parse_mode ='html')


@bot.message_handler(commands=['log'])
def log_message(message):
    if exists(f'log.txt'):
        with open('log.txt','r') as f:
            bot.send_document(message.from_user.id,f)
    else:
        bot.reply_to(message, '<u>Файл с логами отсутствует</u>', parse_mode ='html')


@bot.message_handler(commands=['cleanlog'])
def cleanlog_message(message):
    if exists(f'log.txt'):
        os.remove('log.txt')
        bot.reply_to(message, '<u>Логи почищены</u>', parse_mode ='html')
    else:
        bot.reply_to(message, '<u>Файл с логами отсутствует</u>', parse_mode ='html')


@bot.message_handler()
def get_user_message(message):
    words = message.text.replace(' ','').split('#')
    if words[0] == 'calc':
        ans = Mb.main(message.text)
        bot.reply_to(message, f'Результат вычисления: <b>{ans}</b>', parse_mode ='html')
    else:
        bot.reply_to(message, f'<b>Yo no comprendo que es</b>: {message.text}. Для работы с программой ознакомьтесь со справкой через команду /help', parse_mode ='html')



bot.polling()