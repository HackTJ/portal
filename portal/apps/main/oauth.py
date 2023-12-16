from django.contrib import messages
from social_core.exceptions import AuthForbidden
from social_django.middleware import SocialAuthExceptionMiddleware


class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
        if isinstance(exception, AuthForbidden):
            return "Please log in with your fcpsschools.net account."
        return super().get_message(request, exception)


def post_login(user, request, *args, **kwargs):
    messages.success(request, f"Welcome, {user.username}!")
