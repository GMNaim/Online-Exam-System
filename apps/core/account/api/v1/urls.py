from django.urls import path, include
from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
