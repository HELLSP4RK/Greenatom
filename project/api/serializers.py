from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.models import Group, User, Month
from api.services.create_object import create_user, create_group


class MonthCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Month
        exclude = ['id', 'user']


class UserCreateSerializer(serializers.ModelSerializer):
    dutyDays = MonthCreateSerializer(many=True)

    class Meta:
        model = User
        exclude = ['group']

    def create(self, validated_data):
        day_validated_data = validated_data.pop('dutyDays')
        user = create_user(validated_data)
        day_set_serializer = self.fields['dutyDays']
        for day in day_validated_data:
            day['user'] = user
        day_set_serializer.create(day_validated_data)
        return user


class GroupCreateSerializer(serializers.ModelSerializer):
    usersDutyList = UserCreateSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        user_validated_data = validated_data.pop('usersDutyList')
        group = create_group(validated_data)
        user_set_serializer = self.fields['usersDutyList']
        for user in user_validated_data:
            user['group'] = group
        user_set_serializer.create(user_validated_data)
        return group


class UserSerializer(serializers.ModelSerializer):
    group = SerializerMethodField()

    def get_group(self, obj):
        return obj.group.groupName

    class Meta:
        model = User
        fields = ['group', 'userFullname', 'userEmail', 'userPhone', 'userExt']
