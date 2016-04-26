from django.template.defaulttags import register
from django.db.models.query import QuerySet
import datetime


@register.filter
def get_item(dictionary, key):
    if type(dictionary) == dict:
        return dictionary.get(str(key))
    elif type(dictionary) == QuerySet:
        return dictionary.get(key=key).value


@register.filter
def key_exist(dictionary, key):
    if type(dictionary) == dict or type(dictionary) == QuerySet:
        for i in dictionary:
            if i.key == str(key):
                return True
    return False


@register.filter
def get_range(end=None, start=0):
    return range(start, end)


@register.filter
def get_days(day):
    for item in range(day):
        yield datetime.date.today() + datetime.timedelta(item)


@register.filter
def reservation(dictionary, hour):
    for item in dictionary:
        start_time = item.start_time.hour

        if item.start_time.minute == 30:
            start_time += 0.5
        min_hour = start_time
        max_hour = start_time + item.hour

        if min_hour <= hour < max_hour:
            return True

    return False


@register.filter
def reservation_hour_half(dictionary, hour):
    return reservation(dictionary, hour+0.5)


@register.filter
def day(dictionary, day):
    data = []
    for item in dictionary:
        if day == item.date:
            data.append(item)
    return data

