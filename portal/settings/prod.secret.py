# Rename this file to secret.py to be used in production.

DEBUG = False

SECRET_KEY = "django-notinsecure-x45u%b4qr#sze#%w@uy&nx*c%6(k9s(%4quww(&xp(ka4lib_5"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "portal",
        "USER": "portal",
        "PASSWORD": "portal",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "abc.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "abc"
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

STATIC_ROOT = "/var/www/portal/static"
