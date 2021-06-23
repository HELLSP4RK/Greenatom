from django import template

from table.services.get_queryset import get_users_by_group, get_days_by_user

register = template.Library()


@register.filter
def get_duty_users(group, day):
    all_group_users = [user for user in get_users_by_group(group)]
    users = []
    for user in all_group_users:
        user_days = get_days_by_user(user)
        for check_day in user_days:
            if check_day.day == day and check_day.isDuty:
                users.append(user)
                break
    return users
