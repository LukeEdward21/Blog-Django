from django.http import HttpResponseRedirect
from django.urls import reverse


class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_writer:
            return None
        return reverse('articles:list') 
