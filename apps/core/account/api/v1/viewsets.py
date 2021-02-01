import requests
from django.contrib.auth import authenticate, login as auth_login
from django.db import transaction
from django.shortcuts import reverse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

from apps.core.account.api.v1.serializers import (UserSerializer,
                                                  PermissionSerializer,
                                                  RoleSerializer,
                                                  ResourceSerializer)
from apps.core.account.models import (Permission,
                                      Role,
                                      User,
                                      Resource)
from apps.core.account.permission import UserAccessApiBasePermission
from apps.core.account.viewset import CustomViewSet
from apps.core.base.utils.basics import json_parameter_validation, store_user_activity


@api_view(['POST'])
def registration(request):
    required_params = ['first_name', 'last_name', 'username', 'email' 'password', 'is_active']
    params = request.data

    # validating post data
    if params.get('is_admin') is True:
        required_params.append('secret_code')
    error_param = json_parameter_validation(params, required_params)
    if error_param is not None:
        return Response({"Details": f"'{error_param}' required"}, status=status.HTTP_400_BAD_REQUEST)

    if params.get('is_admin') is True:
        if params.get('secret_code') == settings.SECRET_CODE_ADMIN:
            params['is_staff'] = True
            params['is_superuser'] = True
            del params['is_admin']
            del params['secret_code']
        else:
            return Response({"details": "You are not allowed to be an admin."}, status=status.HTTP_401_UNAUTHORIZED)

    # creating new user
    with transaction.atomic():
        user = User.objects.create_user(**params)

    return Response({"details": "Registration is Successful"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def check_username_existance(request):
    param = request.data
    required_params = ['username']

    # validating data
    error_params = json_parameter_validation(param, required_params)
    if error_params is not None:
        return Response({"details": f"{error_params} required"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(username=param['username'])

    if user.exists():
        return Response({"details": f"{param['username']} already exists"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        return Response({"details": "Valid username"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def check_email_existance(request):
    param = request.data
    required_params = ['email']

    # Validating data
    error_params = json_parameter_validation(param, required_params)
    if error_params is not None:
        return Response({"details": f"{error_params} required"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=param['email'])

    if user.exists():
        return Response({"details": f"{param['email']} already exists."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        return Response({"details": "Valid Email"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def active_user(request, activation_url):
    try:
        user = User.objects.get()
@api_view(['POST'])
def login(request):
    parameters = request.data
    required_parameters = ['email', 'password']
    # validating data
    error_parameters = json_parameter_validation(parameters, required_parameters)  # return the missing parameter
    if error_parameters is not None:
        return Response({"Details": f"{error_parameters} required."}, status=status.HTTP_400_BAD_REQUEST)

    url = f"{request.build_absolute_uri().split('/api')[0]}{reverse('core:account:token_obtain_pair')}"
    token = requests.post(url, json=parameters)
    if token.status_code == 200:
        # Activating session based authentication
        user = authenticate(email=request.data['email'], password=request.data['password'])
        auth_login(request, user)
        # Storing user activity in ActivityLog
        user = User.objects.get(email=request.data['email'])
        store_user_activity(
            request,
            UserSerializer(user).data,
            f"{user.get_full_name()}({user.username}) logged in successfully."
        )
    return Response(token.json(), status=token.status_code)


@api_view(['GET'])
def logout(request):
    pass


class ResourceViewset(CustomViewSet):
    serializer_class = ResourceSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = Resource
    queryset = Resource.objects.all()
    lookup_field = 'hashed_id'


class PermissionViewset(CustomViewSet):
    serializer_class = PermissionSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = Permission
    queryset = Permission.objects.all()
    lookup_field = 'hashed_id'


class RoleViewset(CustomViewSet):
    serializer_class = RoleSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = Role
    queryset = Role.objects.all()
    lookup_field = 'hashed_id'


class UserViewSet(CustomViewSet):
    serializer_class = UserSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = User
    queryset = User.objects.all()
    lookup_field = 'hashed_id'  # Individual object will be found by this field

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')
