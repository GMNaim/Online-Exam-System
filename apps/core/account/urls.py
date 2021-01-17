from django.urls import path, include


app_name = 'account'

urlpatterns = [ 
    path('api/', include('apps.core.account.api.urls')),
]
