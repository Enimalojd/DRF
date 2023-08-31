from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.contrib.auth.models import User
from store.models import Service
from store.serializers import ServiceSerializer, UserSerializer


'''------------------api------------------'''


class UserViewSet(ModelViewSet):
    '''Конечная точка API, которая позволяет просматривать или редактировать пользователей.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceViewSet(ModelViewSet):
    '''Конечная точка API, которая позволяет просматривать или редактировать услуги'''
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price']
    search_fields = ['title', 'price']
    ordering_fields = ['title', 'price']


def auth(request):
    return render(request, 'oauth.html')