from datetime import date
from calendar import LocaleHTMLCalendar
from .models import Event


class Calendar(LocaleHTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, add_today, events):
        # formats a day as a td
        # text danger for today and background warning for event
        events_per_day = events.filter(start_time__day=day)
        if day != 0:
            today = ""
            event_day = ""
            if len(events_per_day) != 0:
                event_day = "bg-warning"
            if add_today is not False:
                if add_today.day == day:
                    today = "text-danger"
            return f"<td class='{event_day}'><span class='date {today}'>{day}</span></td>"
        return '<td></td>'

    def formatweek(self, theweek, add_today, events):
        """ formats a week as a tr """
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, add_today, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, events, withyear=True):
        """ formats a month as a table
        with events for the month"""
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        add_today = False
        today = date.today()
        if (today.month == self.month) and (today.year == self.year):
            add_today = today
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, add_today, events)}\n'
        cal += f'</table>'
        return cal
