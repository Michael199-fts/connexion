from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from api.models import Participant, Sympaty
from connexion.settings import BASE_URL

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name', 'sex', 'email', 'password', 'photo',)

class ParticipantSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, instance):
        if instance.photo:
            return f"{BASE_URL}{instance.photo.url}"
        return ""

    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name', 'sex', 'email', 'photo',)


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sympaty
        fields = ('sender', 'addressee')


class ParticipantsListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, instance):
        if instance.photo:
            return f"{BASE_URL}{instance.photo.url}"
        return ""


    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name', 'sex', 'photo')