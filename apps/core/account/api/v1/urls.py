from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .viewsets import (UserViewSet,
                       PermissionViewset,
                       RoleViewset,
                       ResourceViewset,
                       login,
                       logout)

router = routers.DefaultRouter()
router.register('resource', ResourceViewset)
router.register('permission', PermissionViewset)
router.register('role', RoleViewset)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', login, name='account_login'),
    path('logout/', logout, name='account_logout'),

]
