from django.conf import settings


def template_variables(request):
    variables = {
        'APPLICATION_NAME': settings.APPLICATION_NAME,

    }
    return variables
