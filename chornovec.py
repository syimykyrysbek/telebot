# import telebot
# from googletrans import Translator
# from gtts import gTTS
# import datetime
# # from telebot import types
# token = ''
# bot = telebot.TeleBot(token)
# @bot.message_handler(commands=['start'])
# def message_send(message):
#     bot.send_message(message.chat.id, f'Пивет {message.chat.first_name}. Я перевотчик - бот')

# @bot.message_handler(commands=['alphabet'])
# def alphabet(message):
#     a1 = types.ReplyKeyboardMarkup()
#     a2 = types.KeyboardButton('A')
#     a3 = types.KeyboardButton('B')
#     a4 = types.KeyboardButton('C')
#     a5 = types.KeyboardButton('D')
#     a6 = types.KeyboardButton('E')
#     a1.row(a2, a3, a4)
#     a1.row(a5, a6)
#     bot.send_message(message.chat.id, 'working', reply_markup=a1)
 
# @bot.message_handler(commands=['translator'])
# def message_send2(message):
#     a1 = types.ReplyKeyboardMarkup()
#     en = types.KeyboardButton('en')
#     ru = types.KeyboardButton('ru')
#     ky = types.KeyboardButton('ky')
#     a1.row(en, ru, ky)
#     bot.send_message(message.chat.id, 'Выберите, на какой язык нужна перевести', reply_markup=a1)

# @bot.message_handler(content_types='text')
# def sendMessage(message):
#     translator = Translator()
#     translate_to = translator.translate(message.text, dest='ky').text
#     voice_message = gTTS(translate_to, lang='en', slow=False)       

#     # if message.text == en.text:
    #     translate_to = translator.translate(message.text, dest=en.text).text
    #     voice_message = gTTS(translate_to, lang='en', slow=True)

    # elif message.text == ru.text:
    #         translate_to = translator.translate(message.text, dest=ru.text).text
    #         voice_message = gTTS(translate_to, lang='ru', slow=True)
            
    # elif message.text == ky.text:
    #     translate_to = translator.translate(message.text, dest=ky.text).text
    #     voice_message = gTTS(translate_to, lang='ky', slow=True)
#     file_name = datetime.datetime.now()
#     voice_message.save(f'voses/{file_name}.mp3')
#     voses = open(f'voses/{file_name}.mp3', 'rb')
#     # bot.send_audio(message.chat.id, audio=voses)
#     # bot.send_message(message.chat.id, translate_to)

# print('Бот запушен')
# bot.infinity_polling()





















