from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *
from api.services.get_queryset import get_users_by_day, get_users_by_day_and_group


class DataUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = GroupCreateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            group = serializer.save()
            serializer = GroupCreateSerializer(group, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DutyUsersListView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        day = self.kwargs['day']
        if 'groupId' in self.kwargs:
            return get_users_by_day_and_group(day, self.kwargs['groupId'])
        return get_users_by_day(day)
