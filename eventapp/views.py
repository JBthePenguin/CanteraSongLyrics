from django.shortcuts import render
import calendar
from datetime import timedelta
import datetime
from eventapp.utils import Calendar
from songapp.views import MONTH


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
    month_year = month.split('-')
    day = datetime.datetime(int(month_year[0]), int(month_year[1]), 1)
    event_calendar = Calendar(day.year, day.month)
    context = {
        'event_navbar': 'active',
        'calendar': event_calendar.formatmonth(),
        'month_navbar': MONTH,
        'prev_month': prev_month(day),
        'next_month': next_month(day),
    }
    return render(request, 'eventapp/calendar2.html', context)
