from django.shortcuts import render
import calendar
from django.utils import timezone
from datetime import timedelta
import datetime
from eventapp.utils import Calendar


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = str(next_month.year) + '-' + str(next_month.month)
    return month


def events(request, month):
    # day = timezone.now()
    # print(month)
    month = month.split('-')
    day = datetime.datetime(int(month[0]), int(month[1]), 1)
    event_calendar = Calendar(day.year, day.month)
    context = {
        'calendar': event_calendar.formatmonth(),
        'prev_month': prev_month(day),
        'next_month': next_month(day),
    }
    return render(request, 'eventapp/calendar.html', context)
