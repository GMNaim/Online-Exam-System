from django.urls import path, include
from rest_framework import routers
from .viewsets import UserViewSet, PermissionViewset, RoleViewset


router = routers.DefaultRouter()
router.register('permission', PermissionViewset)
router.register('role', RoleViewset)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
