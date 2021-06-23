from django.shortcuts import render

from table.services.get_object import get_days_list
from table.services.get_queryset import get_groups


def calendar(request):
    days = set(get_days_list())
    groups = get_groups()
    context = {
        'title': 'Календарь',
        'days': days,
        'groups': groups,
    }
    return render(request, 'calendar.html', context=context)
