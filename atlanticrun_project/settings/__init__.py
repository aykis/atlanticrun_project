"""
Django settings for atlanticrun_project project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '172.16.1.244', 'atlanticrun.imt-atlantique.fr']

RECAPTCHA_PRIVATE_KEY = '6Le87UAbAAAAAM8K2WzMi6YGwcThWPtCqRXTe5sY'
RECAPTCHA_PUBLIC_KEY = '6Le87UAbAAAAAEbX6tCNCCOJMEtrKQ1F5S8iPsBi'

# Application definition

INSTALLED_APPS = [
    'index.apps.IndexConfig',
    'envol.apps.EnvolConfig',
    'contact.apps.ContactConfig',
    'inscription.apps.InscriptionConfig',
    'base.apps.BaseConfig',
    'don.apps.DonConfig',
    'decouvrir.apps.DecouvrirConfig',
    'snowpenguin.django.recaptcha2',
    'import_export',
    'modeltranslation',
    #'djstripe',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'atlanticrun_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'atlanticrun_project.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr'
#locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

gettext = lambda s: s
LANGUAGES = (
    ('fr', gettext('Français')),
    ('en', gettext('Anglais')),
)

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TRANSLATABLE_MODEL_MODULES = []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EXPORT_RECORDS_LIMIT = 1000


# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'aykisgeek@gmail.com'
EMAIL_HOST_PASSWORD = 'wtjtsafeefrahkcx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


MAIL_ASF = "testeur"#"atlanticrun.asf@gmail.com"
SECRET_KEY = os.environ.get('SECRET_KEY', 'e*of7=2&e9$q0lci@2(&3rp2(ag(43^=-oz*_ng^a4=772+2=@')

DEBUG = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'atlanticrun',
        'USER': 'malo',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}


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
    'applogfile': {
        'level':'DEBUG',
        'class':'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(BASE_DIR, 'APPNAME.log'),
        'maxBytes': 1024*1024*15, # 15MB
        'backupCount': 10,
        },
    }
}


#STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "pk_test_51JCLABC4qmDCalnooUZolookWJ4zeIFhVvIlEPD3CspjMBDMb1uGf3JmkGp6eZFCnSy0R7qA4WL8ckcBGGGCirqD00Gyg9yt5a")

#DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint
#DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'django': { 
      'format':'django: %(message)s',
    },
  },
  'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/path/to/django/debug.log',
        },
  },
  'loggers': {
    'django': {
        'handlers': ['file'],
        'level': 'DEBUG',
        'propagate': True,
    },
  }
}