from django.urls import path

from table.views import calendar

urlpatterns = [
    path('', calendar),
]