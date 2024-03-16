import os.path

from django.conf import settings
from django.contrib import messages
from social_core.exceptions import AuthForbidden
from social_django.middleware import SocialAuthExceptionMiddleware


try:
    with open(os.path.join(settings.BASE_DIR, "secrets", "user_email_whitelist.txt")) as f:
        USER_WHITELIST = {line.rstrip() for line in f}
except OSError:
    USER_WHITELIST = set()

try:
    with open(os.path.join(settings.BASE_DIR, "secrets", "team_email_whitelist.txt")) as f:
        TEAM_WHITELIST = {line.rstrip() for line in f}
except OSError:
    TEAM_WHITELIST = set()

try:
    with open(os.path.join(settings.BASE_DIR, "secrets", "admin_email_whitelist.txt")) as f:
        ADMIN_WHITELIST = {line.rstrip() for line in f}
except OSError:
    ADMIN_WHITELIST = set()

WHITELIST = USER_WHITELIST | TEAM_WHITELIST | ADMIN_WHITELIST


class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
        if isinstance(exception, AuthForbidden):
            return "Please log in with your fcpsschools.net account."
        return super().get_message(request, exception)


def check_email_whitelist(backend, details, *args, **kwargs):
    # Skip whitelist check in development, unless forced to use
    if settings.DEBUG and not settings.SOCIAL_AUTH_FORCE_USE_WHITELIST:
        return
    # Skip whitelist check in production, only if forced to ignore
    if settings.SOCIAL_AUTH_FORCE_IGNORE_WHITELIST:
        return
    email = details.get("email")
    if email and email in WHITELIST:
        return
    raise AuthForbidden(backend)


def set_permissions(user=None, *args, **kwargs):
    if user:
        if user.email in TEAM_WHITELIST:
            user.is_team = True
            user.is_participant = False
        if user.email in ADMIN_WHITELIST:
            user.is_staff = True
            user.is_superuser = True
            user.is_participant = False
        user.save()


def post_login(user, request, *args, **kwargs):
    messages.success(request, f"Welcome, {user}!")
