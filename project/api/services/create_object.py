from api.models import User, Group


def create_user(data: dict):
    return User.objects.create(**data)


def create_group(data: dict):
    return Group.objects.create(**data)
