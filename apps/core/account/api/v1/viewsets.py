from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from apps.core.account.api.v1.serializers import UserSerializer, PermissionSerializer, RoleSerializer
from apps.core.account.models import User, Permission, Role


class PermissionViewset(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    model = Permission
    queryset = Permission.objects.all()
    lookup_field = 'hashed_id'


class RoleViewset(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    model = Role
    queryset = Role.objects.all()
    lookup_field = 'hashed_id'


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()
    lookup_field = 'hashed_id'  # Individual object will be found by this field

