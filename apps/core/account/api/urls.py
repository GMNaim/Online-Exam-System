from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.core.account.api.v1.urls')),
]
