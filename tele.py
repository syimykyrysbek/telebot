import telebot

token = '5542373742:AAFjCmjRkieLy2mWtPLq0Z5UYxBbRmlox-k'

bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start', 'hi'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')



@bot.message_handler(content_types='text')

def sendMessage(message): 
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')

    elif message.text.lower() == 'как ты?':
        bot.send_message(message.chat.id, 'Нормально сам как?')

    elif message.text.lower() == 'нормально':
        bot.send_message(message.chat.id, 'Аа хорошо')

    elif message.text[0] == '-' and isinstance(int(message.text[1]), int):
        bot.send_message(message.chat.id, 'Отрицателное')

    elif isinstance(int(message.text[0]), int):
        bot.send_message(message.chat.id, 'Положителное')

    else:
        bot.send_message(message.chat.id, message.text.title())
        # print(type(message))

print('Бот запушен')
bot.infinity_polling()



