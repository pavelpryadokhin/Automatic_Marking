import telebot
from data import _token, _BOT_URL

token = _token
BOT_URL = _BOT_URL


def botcheck(screenshot):
    bot = telebot.TeleBot(token, parse_mode=None)
    bot.send_photo(BOT_URL, screenshot)
