import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(func=lambda message: True)
def redirect_message(message):
    if message.chat.id == config.FROM_CHAT_ID_1:
        bot.forward_message(from_chat_id=config.FROM_CHAT_ID_1, chat_id=config.TO_CHAT_ID,
                            message_thread_id=config.TO_MESSAGE_THREAD_ID_1, message_id=message.id)
    elif message.chat.id == config.FROM_CHAT_ID_2:
        bot.forward_message(from_chat_id=config.FROM_CHAT_ID_2, chat_id=config.TO_CHAT_ID,
                            message_thread_id=config.TO_MESSAGE_THREAD_ID_2, message_id=message.id)


bot.polling(non_stop=True)
