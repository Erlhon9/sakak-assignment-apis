from .base import *  # noqa: F403, F401

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "nutrient",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

INSTALLED_APPS += ["drf_yasg"]

DEBUG = True
