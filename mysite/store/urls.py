from django.urls import path

from store.views import profile_view, RegisterView, service_list, service_detail

app_name = 'store'

urlpatterns = [
    path('', service_list, name='service_list'),
    path('<slug:category_slug>/', service_list, name='service_list_category'),
    path('<int:id>/<slug:slug>/', service_detail, name='service_detail'),
    path('profile', profile_view, name='profile'),
    path('register', RegisterView.as_view(), name="register"),

]
