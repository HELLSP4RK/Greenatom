from api.models import Group


def get_groups():
    return Group.objects.all().prefetch_related('usersDutyList', 'usersDutyList__dutyDays')


def get_users_by_group(group):
    return group.usersDutyList.all()


def get_days_by_user(user):
    return user.dutyDays.all()
