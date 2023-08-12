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
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENVIRONMENT = os.getenv("ENVIRONMENT", "PROD")
NGROK_DOMAIN = os.getenv("NGROK_DOMAIN", "*.ngrok-free.app")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "0").lower() in ["true", "t", "1"]

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME'], "www.startyounguk.com", "startyounguk.com",
                 ] if 'WEBSITE_HOSTNAME' in os.environ else ["127.0.0.1", NGROK_DOMAIN]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME'], "https://startyounguk.com", "https://www.startyounguk.com",
                        ] if 'WEBSITE_HOSTNAME' in os.environ else ["https://127.0.0.1", "https://" + NGROK_DOMAIN]


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.contenttypes",
    "django_admin_env_notice",
    "admin_tools_stats",
    "django_nvd3",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home.apps.HomeConfig",
    "contact.apps.ContactConfig",
    "about.apps.AboutConfig",
    "sponsor.apps.SponsorConfig",
    "users.apps.UsersConfig",
    "crispy_forms",
    "crispy_bootstrap5",
    # "bootstrap_modal_forms",
    "phonenumber_field",
    "verify_email.apps.VerifyEmailConfig",
    "captcha",
    "paypal.standard",
    "paypal.standard.ipn",
    "django_otp",
    "django_otp.plugins.otp_totp",
    # 'corsheaders',
    # 'rest_framework',
]

# CORS_ORIGIN_ALLOW_ALL=True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_otp.middleware.OTPMiddleware",
    # 'corsheader.middleware.CorsMiddleware',
]

ROOT_URLCONF = "StartYoungUK.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates", os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django_admin_env_notice.context_processors.from_settings",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
WSGI_APPLICATION = "StartYoungUK.wsgi.application"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "0").lower() in ["true", "t", "1"]
EMAIL_PORT = int(os.getenv("EMAIL_PORT")) # type:ignore
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if ENVIRONMENT == "PROD":
    conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
    conn_str_params = {pair.split('=')[0]: pair.split(
    '=')[1] for pair in conn_str.split(' ')}


    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": conn_str_params["dbname"],
            "USER": conn_str_params["user"],
            "PASSWORD": conn_str_params["password"],
            "HOST": conn_str_params["host"],
        }
    }
else:
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
STATIC_FILES_DIR = (BASE_DIR / "static",)
STORAGES = {
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

# Below line is deprecated in Django>=4.2
# STATIC_FILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files (files uploaded by users have to be persisted)
if ENVIRONMENT == "PROD":
    # Below line is deprecated in Django>=4.2
    #DEFAULT_FILE_STORAGE = 'azure_storage.custom_azure.PublicAzureStorage'

    STORAGES["default"] = {"BACKEND": "storages.backends.azure_storage.AzureStorage"}

    AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
    AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
    AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"
    AZURE_CONTAINER = "media"
    MEDIA_URL = f"{AZURE_CUSTOM_DOMAIN}/{AZURE_CONTAINER}/"
    MEDIA_ROOT = BASE_DIR / "mediafiles"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGIN_REDIRECT_URL = 'user-home' #Temporary redirect to homepage after login

# 2 step mail verification settings
LOGIN_URL = "login"
SUBJECT = "Verify your email to access your Start Young UK Profile"
DEFAULT_FROM_EMAIL = "noreply<no_reply@domain.com>"
EXPIRE_AFTER = "1h"  # Verification Link will expire after one hour from link generation
HTML_MESSAGE_TEMPLATE = (
    BASE_DIR / "templates/email_templates/email_verification.html"
)  # HTML Template for verification email
VERIFICATION_FAILED_TEMPLATE = (
    BASE_DIR / "templates/verification_failure.html"
)  # Path to HTML for failed email verification
REQUEST_NEW_EMAIL_TEMPLATE = (
    BASE_DIR / "templates/resend_verification_email.html"
)  # Path to HTML to render for request new email with link
NEW_EMAIL_SENT_TEMPLATE = (
    BASE_DIR / "templates/new_email_sent.html"
)  # Path to HTML for new email sent


PAYPAL_TEST = os.getenv("PAYPAL_TEST", "0").lower() in ["true", "t", "1"]
PAYPAL_BUY_BUTTON_IMAGE = Path(STATIC_URL, "images", "paypal.png")
PAYPAL_SUBSCRIPTION_BUTTON_IMAGE = Path(STATIC_URL, "images", "paypal.png")

ENVIRONMENT_NAME = "Production Server" if not DEBUG else "Development Server"
ENVIRONMENT_COLOR = "#FF2222" if not DEBUG else "#006400"
ENVIRONMENT_FLOAT = True

# 2FA Name to display on Authenticator App
OTP_TOTP_ISSUER = "Start Young UK Admin"

SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "0").lower() in ["true", "t", "1"]
if SECURE_SSL_REDIRECT:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True

# Cache settings for dashboard
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
#         "LOCATION": "127.0.0.1:11211",
#     }
# }
