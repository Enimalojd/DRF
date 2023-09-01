from django.urls import path

from store.views import profile_view

urlpatterns = [
    path('profile', profile_view, name='profile'),
]
