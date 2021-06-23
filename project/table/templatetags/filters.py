from django import template

register = template.Library()


@register.filter
def get_duty_users(group, day):
    all_group_users = [user for user in group.usersDutyList.all()]
    users = []
    for user in all_group_users:
        user_days = user.dutyDays.all()
        for check_day in user_days:
            if check_day.day == day and check_day.isDuty:
                users.append(user)
                break
    return users
