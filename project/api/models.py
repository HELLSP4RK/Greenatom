import datetime

from django.db.models import *


class Group(Model):

    class Month(IntegerChoices):
        JAN = '1', 'январь'
        FEB = '2', 'февраль'
        MAR = '3', 'март'
        APR = '4', 'апрель'
        MAY = '5', 'май'
        JUNE = '6', 'июнь'
        JULY = '7', 'июль'
        AUG = '8', 'август'
        SEPT = '9', 'сентябрь'
        OCT = '10', 'октябрь'
        NOV = '11', 'ноябрь'
        DEC = '12', 'декабрь'

    YEAR_CHOICES = [(year, year) for year in range(2010, datetime.datetime.now().year + 1)]

    groupId = AutoField(primary_key=True, verbose_name='ID группы')
    groupName = CharField(max_length=100, verbose_name='Наименование')
    # monthName = CharField(max_length=8, choices=MONTH_NAME_CHOICES, verbose_name='Название месяца')
    monthNumber = SmallIntegerField(choices=Month.choices, verbose_name='Месяц')
    year = SmallIntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return f'{self.groupId} | {self.groupName}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class User(Model):
    userName = CharField(max_length=20, unique=True, verbose_name='Логин')
    userFullname = CharField(max_length=60, verbose_name='ФИО')
    userId = AutoField(primary_key=True, verbose_name='ID пользователя')
    userEmail = EmailField(unique=True, verbose_name='Email')
    userPhone = CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    userExt = CharField(max_length=20, blank=True, null=True, verbose_name='Добавочный')
    isOwner = BooleanField(verbose_name='Руководитель группы')
    group = ForeignKey(Group, on_delete=CASCADE, related_name='usersDutyList', verbose_name='Группа')

    def __str__(self):
        return f'{self.userId} | {self.userName}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Month(Model):

    class DayOfWeek(TextChoices):
        MON = 'Пн', 'Понедельник'
        TUE = 'Вт', 'Вторник'
        WED = 'Ср', 'Среда'
        THU = 'Чт', 'Четверг'
        FRI = 'Пт', 'Пятница'
        SAT = 'Сб', 'Суббота'
        SUN = 'Вс', 'Воскресенье'

    DAY_CHOICES = [(day, day) for day in range(1, 31 + 1)]

    user = ForeignKey(User, on_delete=CASCADE, related_name='dutyDays', verbose_name='Пользователь')
    day = SmallIntegerField(choices=DAY_CHOICES, verbose_name='Число')
    dayOfWeek = CharField(max_length=2, choices=DayOfWeek.choices, verbose_name='День недели')
    isDuty = BooleanField(verbose_name='Дежурство')

    def __str__(self):
        return f'{self.id} | {self.user.userName}'

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
