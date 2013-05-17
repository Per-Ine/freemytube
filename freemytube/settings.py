# Django settings for freemytube project.
import os

location = lambda x: os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('per-ine', 'perez.k1@orange.fr'),
    ('Julien Maupetit', 'julien@maupetit.me'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'fmtDB.sqlite',
        'USER': 'per-ine',
        'PASSWORD': '118131',
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = location('public/media')
MEDIA_URL = '/media/'

STATIC_ROOT = location('public/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '22=2oc47e@r&3v1p+djh_c(+-dc#lif6q8v3w^wvm0cfug#ymv'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'freemytube.urls'

WSGI_APPLICATION = 'freemytube.wsgi.application'

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',

    # Free My Tube
    'core',

    'django.contrib.admin',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

REST_FRAMEWORK = {
    'PAGINATE_BY': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
}
