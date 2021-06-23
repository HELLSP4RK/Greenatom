from api.models import User


def get_users_by_day(day):
    return User.objects.filter(dutyDays__day=day, dutyDays__isDuty=True)


def get_users_by_day_and_group(day, groupId):
    return get_users_by_day(day).filter(group=groupId)
