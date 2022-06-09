import telebot
import requests

token = '5353404817:AAFgZ6iNA-a-5R4VwRK5eL2-6n85D7GoWQs'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def message_send(message):
    bot.send_message(message.chat.id, f'Пивет {message.chat.first_name}. Я covid19 - бот')

@bot.message_handler(content_types='text')
def sendMessage(message): 
    print(message.text)
    url = f'https://covid-api.mmediagroup.fr/v1/cases?country={message.text.title()}'
    response= requests.get(url)
    data = response.json()
    a = f"Население {message.text.title()} : {data['All']['confirmed']}"
    b = f"выздоровел {message.text.title()} : {data['All']['recovered']}"
    v = f"летальные исходы {message.text.title()} : {data['All']['deaths']}"
    g = f"страна {message.text.title()} : {data['All']['country']}"
    d = f"Население {message.text.title()} : {data['All']['population']}"
    bot.send_message(message.chat.id, f' {a}\n{b}\n{v}\n{g}\n{d}')

print('Бот запушен')
bot.infinity_polling()
