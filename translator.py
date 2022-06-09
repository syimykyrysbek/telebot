import telebot
from googletrans import Translator
from gtts import gTTS
import datetime

token = '5145775438:AAGnX5G2mvGAq78W_qQvV0u8FeFVg7kA_mE'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def message_send(message):
    bot.send_message(message.chat.id, f'Пивет {message.chat.first_name}. Я перевотчик - бот')

@bot.message_handler(content_types='text')
def sendMessage(message):
    translator = Translator()
    translate_to = translator.translate(message.text, dest='ky').text
    voice_message = gTTS(translate_to, lang='ky', slow=False)       
    file_name = datetime.datetime.now()
    voice_message.save(f'voses/{file_name}.mp3')
    voses = open(f'voses/{file_name}.mp3', 'rb')
    bot.send_audio(message.chat.id, audio=voses)
    bot.send_message(message.chat.id, translate_to)

print('Бот запушен')
bot.infinity_polling()





















