import telebot
import requests
from googletrans import Translator

token = '5547631812:AAFKBS62Jf13_gtw7evt7m_f2ieT2DulN3I'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def message_send(message):
    bot.send_message(message.chat.id, f'Пивет {message.chat.first_name}. Я погода - бот')

@bot.message_handler(content_types='text')
def sendMessage(message): 
    API_KEY = 'b6fad32d53b445047b0498e182aebaef'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API_KEY}&units=metric'
    response= requests.get(url)
    data = response.json()
    translator = Translator()

    a = data['weather'][0]['icon']
    w_cond = translator.translate(data['weather'][0]['description'], dest='ru').text
    weather = f"Погода в городе {message.text.title()}: {w_cond}"

    tem = translator.translate(data['main']['temp'], dest='ru').text
    temp = f"Темперура в городе {message.text.title()}:{tem}℃"

    cond = translator.translate(data['weather'][0]['main'], dest='ru').text
    coudd = f"Прагноз пагоды в городе {message.text.title()}:{cond}"

    feels_like = f"Температура в городе {message.text.title()} ощущается как:{data['main']['feels_like']}℃"
    min_temp = f"Минималная температура в городе {message.text.title()} : {data['main']['temp_min']}℃"
    max_temp = f"Максималная температура в городе {message.text.title()} : {data['main']['temp_max']}℃"

    bot.send_message(message.chat.id, f'{weather}\n{temp}\n{coudd}\n{feels_like}\n{min_temp}\n{max_temp}')
    bot.send_photo(message.chat.id, f'http://openweathermap.org/img/wn/{a}@2x.png')
print('Бот запушен')
bot.infinity_polling()

