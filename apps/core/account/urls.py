from django.urls import path, include
from .views import (registration,
                    logout,
                    login,
                    reset,
                    change_password)

app_name = 'account'

urlpatterns = [ 
    path('api/', include('apps.core.account.api.urls')),
    path('registration', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('reset/', reset, name='reset'),
    path('change-password', change_password, name='change_password'),
]
