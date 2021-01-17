from django.urls import path, include


app_name = 'base'

urlpatterns = [ 
    path('api/', include('apps.core.base.api.urls')),
]
