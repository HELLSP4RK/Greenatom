from api.models import Month


def get_days_list():
    return Month.objects.values_list('day', flat=True)
