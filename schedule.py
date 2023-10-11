import datetime

schedule = {1: [{15: 30}, {17: 20}, {19: 5}, {20: 50}], 2: [{8: 0}, {9: 50}, {11: 40}, {13: 40}],
            3: [{8: 0}, {15: 30}, {17: 20}, {19: 5}]}

now = datetime.datetime.now()  # текущие дата и время
day_today = datetime.datetime.isoweekday(now)  # текущий день - его номер
shedule_day = schedule[day_today]
while shedule_day:  # расписание на день
    next_lesson = shedule_day.pop(0)
    while True:
        if next_lesson[now.hour] == now.minute:

# Сколько ждать осталось
days_to_wait = (target_day - day_today + 6) % 7
hours_to_wait = 24 - now.hour - 1
munutes_to_wait = 60 - now.minute - 1
seconds_to_wait = 60 - now.second - 1
