from .base import *  # noqa: F403, F401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     # 'formatters': {
#     #     'verbose': {
#     #         'format': '{levelname} {asctime} {module} {message}',
#     #         'style': '{',
#     #     },
#     # },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',  # 원하는 로그 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#             'class': 'logging.StreamHandler',
#             # 'formatter': 'verbose',  # 사용자 정의한 로그 포맷 지정
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG',  # Django ORM에 대한 SQL 쿼리 로깅 레벨 설정
#             'propagate': False,
#         },
#     },
# }