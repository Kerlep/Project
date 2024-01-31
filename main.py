import telebot

bot = telebot.TeleBot('токен')

# Обработчик текста
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


# Обработчик изображений
@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    bot.send_photo(message.chat.id, message.photo.file_id)

# Обработчик стикеров
@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

# Запуск бота
bot.polling()

