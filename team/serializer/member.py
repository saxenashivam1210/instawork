from rest_framework import serializers
from team.models.member import Member as memberModel
import uuid


class Member(serializers.ModelSerializer):
    class Meta:
        model = memberModel
        fields = ['uuid', 'first_name', 'last_name', 'phone_number', 'email', 'role']

    def create(self, validated_data):
        instance = memberModel()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.phone_number = validated_data.get('phone_number')
        instance.role = validated_data.get('role', 'regular')
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.uuid = validated_data.get('uuid', instance.uuid)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.role = validated_data.get('role', instance.role)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
