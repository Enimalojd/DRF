from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from store.models import Service, UserServiceRelation, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ServiceSerializer(ModelSerializer):
    '''Сериализация услуг'''

    class Meta:
        model = Service
        fields = '__all__'


class UserServiceRelationSerializer(ModelSerializer):
    '''Сериализация оценок'''

    class Meta:
        model = UserServiceRelation
        fields = ('service', 'like', 'in_bookmark', 'rate')


class CategoriesSerializer(ModelSerializer):
    '''Сериализация категорий товаров'''

    class Meta:
        model = Category
        fields = '__all__'
