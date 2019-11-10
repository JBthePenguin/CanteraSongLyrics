from django.shortcuts import render
import calendar
from datetime import timedelta, datetime
from eventapp.utils import Calendar
from songapp.views import MONTH
from eventapp.models import Event


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
    day = datetime(int(month_year[0]), int(month_year[1]), 1)
    events = Event.objects.filter(
        start_time__year=day.year, start_time__month=day.month).order_by(
        "start_time")
    event_calendar = Calendar(day.year, day.month)
    context = {
        'event_navbar': 'active',
        'calendar': event_calendar.formatmonth(events),
        'month_navbar': MONTH,
        'prev_month': prev_month(day),
        'next_month': next_month(day),
        'events': events,
    }
    return render(request, 'eventapp/calendar.html', context)
