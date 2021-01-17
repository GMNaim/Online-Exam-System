from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('exam/', include('apps.exam.urls')),
]
