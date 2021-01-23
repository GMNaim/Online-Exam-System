from django.urls import path, include
from .views import dashboard


app_name = 'base'

urlpatterns = [ 
    path('api/', include('apps.core.base.api.urls')),
    path('', dashboard, name='dashboard'),
]
