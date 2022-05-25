"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime
import locale
from datetime import timedelta, datetime, date, time

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
    date_yestoday = date.today() + timedelta(days=-1)
    date_30 = date.today() + timedelta(days=-30)
    print(f'Вчера: {(date_yestoday).strftime("%A %d %B %Y")}, сегодня: {date.today().strftime("%A %d %B %Y")}, 30 дней назад: {(date_30).strftime("%A %d %B %Y")}')

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    text_date = "01/01/20 12:10:03.234567"
    x = datetime.strptime(text_date, '%m/%d/%y %H:%M:%S.%f')
    return x

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
