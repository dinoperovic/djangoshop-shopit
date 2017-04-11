"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Make shopit module accessible.
sys.path.insert(0, os.path.dirname(BASE_DIR))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xmiwlkr70oikq=3py@j2knaelu4zher9s%$-$k6twsz*o&rklo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'email_auth',  # required by django-shop.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # django-cms
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',

    # django-shop
    'adminsortable2',
    'cmsplugin_cascade',
    'django_fsm',
    'fsm_admin',
    'post_office',
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'shop',

    # shopit
    'parler',
    'shopit',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'shop.middleware.CustomerMiddleware',
    'shop.middleware.MethodOverrideMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'shop.context_processors.customer',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

SILENCED_SYSTEM_CHECKS = ['auth.W004']

FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures')]


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Authentication
AUTH_USER_MODEL = 'email_auth.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LOGIN_URL = 'shopit-account-login'
LOGOUT_URL = 'shopit-account-logout'
LOGIN_REDIRECT_URL = 'shopit-account-detail'


# Email
EMAIL_BACKEND = 'post_office.EmailBackend'


# Internationalization, parler
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = [
    ('en', 'English'),
]
PARLER_LANGUAGES = {
    1: tuple({'code': x[0]} for x in LANGUAGES),
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# cms
CMS_TEMPLATES = [
    ('default.html', 'Default'),
]
CMS_PLACEHOLDER_CONF = {
    'content': {
        'plugins': ['TextPlugin'],
        'name': 'Content',
    }
}


# filer
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# rest_framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'shop.rest.money.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12,
}
SERIALIZATION_MODULES = {'json': 'shop.money.serializers'}
COERCE_DECIMAL_TO_STRING = True


# shop
SHOP_APP_LABEL = 'shopit'
SHOP_PRODUCT_SUMMARY_SERIALIZER = 'shopit.serializers.ProductSummarySerializer'
SHOP_CART_MODIFIERS = [
    'shop.modifiers.defaults.DefaultCartModifier',
    'shopit.modifiers.ShopitCartModifier',
    'shopit.modifiers.PayInAdvanceModifier',
    'shop.modifiers.defaults.SelfCollectionModifier',
]
SHOP_ORDER_WORKFLOWS = [
    'shop.payment.defaults.PayInAdvanceWorkflowMixin',
    'shop.payment.defaults.CancelOrderWorkflowMixin',
    'shopit.shipping.ShippingWorkflowMixin',
]


# shopit
SHOPIT_FILTER_ATTRIBUTES_INCLUDES_VARIANTS = True
