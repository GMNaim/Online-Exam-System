from rest_framework.permissions import BasePermission


class UserAccessApiBasePermission(BasePermission):
    def __init__(self, model):
        self.model = model
        super(UserAccessApiBasePermission, self).__init__()

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return self.has_object_permission(request, view, self.model)

    def has_object_permission(self, request, view, obj):
        if request.user.role.id == 1:
            # *** super_admin can do all action(all permissions)
            permissions = [_ for i in request.user.role.permission.all().values_list('code') for _ in i]
            # permissions = []
            # for permsn in request.user.role.permission.all().values_list('code'):
            #     type(permsn) = tuple
            #     for i in permsn:
            #         permissions.append(i)

        else:
            # *** Others have only the active permissions
            permissions = [p for permisn in request.user.role.permission.filter(is_active=True).value_list('code') for p
                           in permisn]
        app_label = str(obj._meta.app_label)  # getting the app name
        object_class_name = str(obj._meta.model_name)  # getting the model name
        app_label_class_name = app_label + '_' + object_class_name  # Example: account_resource
        has_operation_permissions = [p.split('.')[0] for p in permissions if  # ex: add.account_resource
                                     app_label_class_name in p]  # ex: [add, self_view, delete]

        action_methods = {
            'detail_view': ['GET'],
            'self_view': ['GET'],
            'list_view': ['GET'],
            'add': ['POST'],
            'change': ['PUT', 'PATCH'],
            'delete': ['DELETE']
        }
        for operation_permission in has_operation_permissions:
            if request.method in action_methods[operation_permission]:
                return True
        return False
