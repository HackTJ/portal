# Rename this file to secret.py to be used in production.

DEBUG = False

SECRET_KEY = "django-notinsecure-x45u%b4qr#sze#%w@uy&nx*c%6(k9s(%4quww(&xp(ka4lib_5"

# Set below to 63072000 (2 years) when we are confident that certificate renewal works
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

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

# Cookie Security Settings

CSRF_COOKIE_SECURE = True
LANGUAGE_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_HTTPONLY = True
LANGUAGE_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SAMESITE = "None"
LANGUAGE_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SAMESITE = "None"
