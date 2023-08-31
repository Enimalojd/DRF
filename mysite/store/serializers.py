from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from store.models import Service


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ServiceSerializer(ModelSerializer):
    '''Сериализация услуг'''

    class Meta:
        model = Service
        fields = '__all__'
