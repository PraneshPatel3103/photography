from django.shortcuts import render
from .models import DateLink
import calendar
from datetime import date

def calendar_view(request, year=None, month=None):
    today = date.today()
    if year is None: 
        year = today.year
    if month is None: 
        month = today.month

    cal = calendar.Calendar()
    month_days = cal.itermonthdates(year, month)
    links = {dl.date: dl.url for dl in DateLink.objects.filter(date__year=year, date__month=month)}

    # Filter out days that are not in the current month
    month_days = [d for d in month_days if d.month == month]

    context = {
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'month_days': [(d, links.get(d)) for d in month_days],
        'weekdays': ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    }

    return render(request, 'calendar_app/calendar.html', context)
