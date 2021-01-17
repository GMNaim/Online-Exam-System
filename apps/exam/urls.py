from django.urls import path, include


app_name = 'exam'

urlpatterns = [ 
    path('api/', include('apps.exam.api.urls')),

]
