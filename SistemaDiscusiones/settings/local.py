from .base import * #el punto undica que esta en el mismo directorio

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER':'enrique',
        'PASSWORD': 'Anlleck1234',
        'HOST':'localhost',
        'PORT':'5432',
    }
}
STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

