from datetime import datetime


def str_time_to_datetime(cls, str_time):
    return datetime.strptime(str_time, '%H:%M')


def str_date_to_datetime(cls, str_date):
    return datetime.strptime(str_date, '%Y-%m-%d')