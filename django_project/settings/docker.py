from .base import *  # noqa: F403, F40

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "nutrient",
        "USER": "root",
        "PASSWORD": "XLKyXGsWY5DzFqfXQWHYtUzXbFwQROjV",
        "HOST": "postgres",
        "PORT": "5432",
    }
}
