from botclick import botclick
from schedule import schedule
from telegrambot import botcheck
from PIL import Image

import datetime
import time

login = 'mrpavel23ooo@mail.ru'
password = 'v234praw'


def main():
    while True:
        now = datetime.datetime.now()  # текущие дата и время
        day_today = datetime.datetime.isoweekday(now)  # текущий день - его номер
        hours_to_wait = 24 - now.hour - 1
        munutes_to_wait = 60 - now.minute - 1
        seconds_to_wait = 60 - now.second - 1
        if day_today not in schedule:  # eсли день нет в списке в следующий день
            time.sleep(hours_to_wait * 3600 + munutes_to_wait * 60 + seconds_to_wait)
            continue
        shedule_day = schedule[day_today]
        while shedule_day:  # расписание на день
            next_lesson = shedule_day.pop(0)
            print((next_lesson[0] - now.hour - 1) * 3600 + (60 - now.minute + next_lesson[1] + 25) * 60)
            timesleep=(next_lesson[0] - now.hour) * 3600 + (abs(next_lesson[1] - now.minute + 15)) * 60
            if timesleep>0:
                time.sleep(timesleep)
            result = botclick(login, password)
            botcheck(result)
        hours_to_wait = 24 - now.hour - 1
        munutes_to_wait = 60 - now.minute - 1
        seconds_to_wait = 60 - now.second - 1
        time.sleep(hours_to_wait * 3600 + munutes_to_wait * 60 + seconds_to_wait)


if __name__ == "__main__":
    main()
