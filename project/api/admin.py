from django.contrib import admin

from api.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    pass
