from django.shortcuts import render

from api.models import Month, Group


def calendar(request):
    days = set(Month.objects.values_list('day', flat=True))
    groups = Group.objects.all().prefetch_related('usersDutyList', 'usersDutyList__dutyDays')
    context = {
        'title': 'Календарь',
        'days': days,
        'groups': groups,
    }
    return render(request, 'calendar.html', context=context)
