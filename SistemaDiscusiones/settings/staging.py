from .base import * #el punto undica que esta en el mismo directorio

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7pem0lp9e5ekk',
        'USER':'xwdzomvghcyfdd',
        'PASSWORD': '3XB63wOXDRYljgwgNvgQs9UU0R',
        'HOST':'ec2-54-235-147-211.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
