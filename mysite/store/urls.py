from django.urls import path

from store.views import profile_view, RegisterView

app_name = 'store'

urlpatterns = [
    path('profile', profile_view, name='profile'),
    path('register', RegisterView.as_view(), name="register"),

]
