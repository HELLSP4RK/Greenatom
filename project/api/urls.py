from django.urls import path

from api.views import *

urlpatterns = [
    path('upload/', DataUploadView.as_view()),
    path('duty/day=<int:day>/', DutyUsersListView.as_view()),
    path('duty/day=<int:day>/groupid=<int:groupId>/', DutyUsersListView.as_view()),
]
