from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from apps.core.account.api.v1.serializers import UserSerializer
from apps.core.account.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()
