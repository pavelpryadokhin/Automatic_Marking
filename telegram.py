import telebot
import time
from datetime import datetime

bot = telebot.TeleBot("TOKEN", parse_mode=None)
BOT_URL = "URL"

now = datetime.now()
current_time = now.strftime("%H:%M")

# Запускаем цикл для проверки времени
while True:
    time.sleep(1)
    if current_time == '12:00':  # Выставляете ваше время
        print('pass')
        bot.send_photo(BOT_URL, open('pass.png', 'rb'))

bot.infinity_polling()
