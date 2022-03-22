from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from api.models import Participant, Sympaty


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name', 'sex', 'email', 'password', 'photo',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegistrationSerializer, self).create(validated_data)

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sympaty
        fields = ('sender', 'addressee')