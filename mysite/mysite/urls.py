from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers



from store.views import ServiceViewSet, UserViewSet, auth

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('', include('social_django.urls', namespace='social')),
    re_path('auth', auth)
]

urlpatterns += router.urls
