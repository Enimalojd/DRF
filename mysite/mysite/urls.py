from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from store.views import ServiceViewSet, UserViewSet, mainpage_view

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    re_path('', include('social_django.urls', namespace='social')),
    path('store/', include('store.urls', namespace='store')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', mainpage_view, name='mainpage')
]


urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

