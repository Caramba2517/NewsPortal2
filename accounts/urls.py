from django.urls import path, include
from .views import IndexView, upgrade_me


urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', IndexView.as_view(), name='profile'),
    path('upgrade/', upgrade_me, name='upgrade')
]