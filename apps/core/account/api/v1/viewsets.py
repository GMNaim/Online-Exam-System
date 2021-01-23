import requests
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import reverse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.core.account.api.v1.serializers import UserSerializer, PermissionSerializer, RoleSerializer
from apps.core.account.models import Permission, Role, User
from apps.core.base.utils.basics import json_parameter_validation


@api_view(['POST'])
def login(request):
    parameters = request.data
    required_parameters = ['username', 'password']
    # validating data
    error_parameters = json_parameter_validation(parameters, required_parameters)  # return the missing parameter
    if error_parameters is not None:
        return Response({"Details": f"{error_parameters} required."}, status=status.HTTP_400_BAD_REQUEST)

    url = f"{request.build_absolute_uri().split('/api')[0]}{reverse('core:account:token_obtain_pair')}"
    print(url, '-0-----', reverse('core:account:token_obtain_pair'))
    token = requests.post(url, json=parameters)
    if token.status_code == 200:
        # Activating session based authentication
        user = authenticate(username=request.data['username'], password=request.data['password'])
        auth_login(request, user)

    return Response(token.json(), status=token.status_code)


@api_view(['GET'])
def logout(request):
    pass


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
