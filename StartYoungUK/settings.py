"""
Django settings for StartYoungUK project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e-5dkhxdgkp#e1+!*^*px4lpic+8d#!m0g(pfqw7&hc0y=2xpk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'contact.apps.ContactConfig',
    'about.apps.AboutConfig',
    'sponsor.apps.SponsorConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'bootstrap_modal_forms',
    'phonenumber_field',
    'verify_email.apps.VerifyEmailConfig',
    'captcha',
    # 'corsheaders',
    # 'rest_framework',
]

# CORS_ORIGIN_ALLOW_ALL=True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'corsheader.middleware.CorsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'StartYoungUK.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
WSGI_APPLICATION = 'StartYoungUK.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'youngcoders.codefest@gmail.com'
EMAIL_HOST_PASSWORD = 'dnziblkvhptubmfa'

DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'
EXPIRE_AFTER = "1h" # Verification Link will expire after one hour from link generation

RECAPTCHA_PUBLIC_KEY = '6LdilSsiAAAAALkeAdLLWLiqUkdxTvoS3k7OqzyN'
RECAPTCHA_PRIVATE_KEY = '6LdilSsiAAAAACxlSATIX41xQyg9VAc9RqjTtaXy'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : BASE_DIR / 'db.sqlite3',
        #'ENGINE': 'sql_server.pyodbc',
        # 'ENGINE' : 'mssql',
        # 'NAME' : 'StartYoungUK',
        # 'USER': 'youngcoders-admin',
        # 'PASSWORD' : 'Codefest#123',
        # 'HOST': 'youngcoders.database.windows.net',
        # 'OPTIONS': {
        #     'driver': 'ODBC Driver 18 for SQL Server',
            # 'isolation_level': 'READ_UNCOMMITTED',
        # }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATIC_FILES_DIR = (
    os.path.join(BASE_DIR, 'static'),    
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'user-home' #Temporary redirect to homepage after login
LOGIN_URL = "login"
SUBJECT = "Verify your email to access your StartYoungUK Dashboard"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CSRF_TRUSTED_ORIGINS = ['https://startyounguk2.azurewebsites.net']
