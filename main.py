import telebot

TOKEN = "8606042874:AAGVbfBwIg13FPfPnl_inVaFVb2w8B7geDU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Hey... I'm here 😏")

bot.infinity_polling()
