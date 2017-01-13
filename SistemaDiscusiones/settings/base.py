from unipath import Path
import os
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
BASE_DIR = Path(__file__).ancestor(3)
SECRET_KEY = '(vg(gx)0zi6zs(y8)uy+$!5j$2-wn=hfp2kh9rq&jv7fbop@8'

DJANGO_APPS=(
'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS=(
    'south',
    'social.apps.django_app.default'
)

LOCAL_APPS=(
    'apps.home',
    'apps.users',
    'apps.courses'
)

INSTALLED_APPS =DJANGO_APPS+THIRD_PARTY_APPS+LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS=[BASE_DIR.child('templates')]

#modelo personalizado aplicacion.modelo
AUTH_USER_MODEL='users.User'

#formas de autentificacion
AUTHENTICATION_BACKENDS=(
'social.backends.facebook.FacebookAppOAuth2',
'social.backends.facebook.FacebookOAuth2',
'social.backends.twitter.TwitterOAuth',
'django.contrib.auth.backends.ModelBackend',
)

#parametros para facebook
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/panel'
SOCIAL_AUTH_LOGIN_URL='/error/'
SOCIAL_AUTH_USER_MODEL= 'users.User'
SOCIAL_AUTH_FACEBOOK_SCOPE=['email']


#pipelines default and custom
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.mail.mail_validation',
    'apps.users.pipelines.get_avatar',
    
   
)
#lleves de acceso para las aplicaciones de facebook y twiter
SOCIAL_AUTH_FACEBOOK_KEY='114503395552683'
SOCIAL_AUTH_FACEBOOK_SECRET='48e2057a50b7054ac4db05dfda2e4594'
