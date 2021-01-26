import operator
from functools import reduce
from django.db.models import Q
from rest_framework import viewsets


class CustomViewSet(viewsets.ModelViewSet):
    model = None
    change_keys = None
    search_keywords = None
    queryset = None
    query = None

    def get_queryset(self):
        if self.model is None:
            raise AssertionError('CustomViewSetForQuerySet Need to include a model.')
        self.query = self.object_level_permission()

        return self.query

    def get_permissions(self):
        for permission in self.permission_classes:
            if permission.__name__ == 'UserAccessApiBasePermission':
                return [permission(self.model)]

    def object_level_permission(self):
        """ Defining user can see what depending on role """
        user_permissions = self.request.user.role.permission.values_list('code', flat=True)
        app_label = str(self.model._meta.app_label)
        object_class_name = str(self.model._meta.model_name)
        app_label_class_name = app_label + '_' + object_class_name
        queryset = self.model.objects.filter()

        if app_label_class_name in ['account_resource']:
            if self.request.user.role.code in ['super_admin']:
                queryset = self.model.objects.all()
            elif 'list_view.account_resource' in user_permissions:
                queryset = self.model.objects.filter(is_active=True)
            elif 'self_view.account_resource' in user_permissions:
                view_permissions = self.request.user.role.permission.filter(code__contains='view.').values_list(
                    'resource_id', flat=True)
                print(view_permissions)
                queryset = self.model.objects.filter(is_active=True, permission_resource__in=view_permissions)
            else:
                queryset = self.model.objects.none()

        if app_label_class_name == 'account_permission':
            if self.request.user.role.code in ['super_admin']:
                queryset = self.model.objects.all()
            elif 'list_view.account_permission' in user_permissions:
                queryset = self.model.objects.filter(is_active=True, resource__is_active=True)
            elif 'self_view.account_permission' in user_permissions:
                queryset = self.model.objects.filter(is_active=True, id__in=self.request.user.role.permission.all())
            else:
                queryset = self.model.objects.none()

        if app_label_class_name == 'account_role':
            if self.request.user.role.code in ['super_admin']:
                queryset = self.model.objects.all()
            elif 'list_view.account_role' in user_permissions:
                queryset = self.model.objects.filter(~Q(id=1))  # admin can see all roles except role_id=1 or super_user
            elif 'self_view.account_role' in user_permissions:
                queryset = self.model.objects.filter(id=self.request.user.role.id)
            else:
                queryset = self.model.objects.none()

        if app_label_class_name == 'account_user':
            if self.request.user.role.code in ['super_admin']:
                queryset = self.model.objects.all()
            elif 'list_view.account_user' in user_permissions:
                queryset = self.model.objects.filter(~Q(role_id=1))
            elif 'self_view.account_user' in user_permissions:
                queryset = self.model.objects.filter(id=self.request.user.id)
            else:
                queryset = self.model.objects.none()

        return queryset

