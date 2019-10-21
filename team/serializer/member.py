from rest_framework import serializers
from team.models.member import Member as memberModel
import uuid


class Member(serializers.ModelSerializer):
    class Meta:
        model = memberModel
        fields = ['uuid', 'first_name', 'last_name', 'phone_number', 'email', 'role']

    def create(self, data):
        instance = memberModel()
        instance.uuid = uuid.uuid4()
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.phone_number = data.get('phone_number', instance.phone_number)
        instance.role = data.get('role', instance.role)
        instance.email = data.get('email', instance.email)
        instance.save()
        return instance

    def update(self, instance, data):
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.phone_number = data.get('phone_number', instance.phone_number)
        instance.role = data.get('role', instance.role)
        instance.email = data.get('email', instance.email)
        instance.save()
        return instance
