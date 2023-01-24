import telebot

bot = telebot.TeleBot("5876255273:AAFsjaaCFqSKZzGkrwDxAEJl8kWGBfVjhJ0")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message.chat.id, "Пошел на хуй")
    if "Тима" in message.text:
        bot.send_message("Тима суси")


bot.infinity_polling()