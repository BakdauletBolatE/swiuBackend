from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = '+v6-04zu!l#h&+p4f(u^un@(+^u0oa$ew2nfs4w5_m=rb=41$d'


try:
    from .local import *
    DEBUG = True
except ImportError as e:
    DEBUG = False


if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['192.168.32.76', 'localhost','swiu.online']




INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'faculties',
    'departments',
    'staff',
    'news',
    'library',
    'ckeditor',
    'changeuniver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
X_FRAME_OPTIONS = 'SAMEORIGIN'


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'swiu',
            'USER': 'postgres',
            'PASSWORD': '2580',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'swiu',
        'USER': 'bbb',
        'PASSWORD': 'bagivox123F',
        'HOST': 'localhost',
        'PORT':''
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'kk'

gettext = lambda s: s

LANGUAGES = (
    ('ru', gettext('Russia')),
    ('en',gettext('English')),
    ('kk',gettext('Kazakhstan')),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'




CKEDITOR_CONFIGS = {
    'default': {
        'skin':'office2013'
        
    }
}

        
CKEDITOR_UPLOAD_PATH = "uploads/"
