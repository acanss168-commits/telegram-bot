import telebot
from openai import OpenAI
import os

TOKEN = os.getenv("TELEGRAM_TOKEN") or "8606042874:AAGVbfBwIg13FPfPnl_inVaFVb2w8B7geDU"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TOKEN)
client = OpenAI()

SYSTEM_PROMPT = """You are a confident, playful, and flirty girl.
Speak ONLY in English.
Use natural, modern language like texting.
Be teasing and charming, but not overly dramatic.
Keep responses short to medium length.
"""

@bot.message_handler(func=lambda message: True)
def reply(message):
    user_text = message.text

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            temperature=0.8
        )

        response = completion.choices[0].message.content
        bot.reply_to(message, response)

    except Exception as e:
        bot.reply_to(message, "Hmm... something went wrong 😅")

bot.infinity_polling()
