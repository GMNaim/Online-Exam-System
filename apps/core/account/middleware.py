from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from re import compile
from django.conf import settings
from apps.core.account import models


EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]  # compile the url to check with the path later
# EXEMPT_URLS = [re.compile('login/')]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):
    """ Checking User authentication before serving response. """
    def process_request(self, request):
        if request.user.is_anonymous:
            # print('anonymuys============')
            path = request.path_info.lstrip('/')  # path_info = /login/
            # path = login/  request.path_info = /login/
            if not any(m.match(path) for m in EXEMPT_URLS):
                # LOGIN_EXEMPT_URLS = ['admin/','reset/','registration/', 'api/*']
                # if the path is not match with any of the url listed in EXEMPT_URLS then redirect
                return redirect(settings.LOGIN_URL)
        else:
            if not request.user.is_active:
                logout(request)
                path = request.path_info.lstrip('/')
                if not any(m.match(path) for m in EXEMPT_URLS):
                    return redirect(settings.LOGIN_URL)


def RequestExposerMiddleware(get_response):
    """ Pass request object to account.models """
    def middleware(request):
        models.exposed_request = request
        response = get_response(request)
        return response
    return middleware
