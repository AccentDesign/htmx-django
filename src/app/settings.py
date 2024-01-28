from os import environ
from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))


# Security

SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = []
ALLOWED_HOSTS += environ.get("ALLOWED_HOSTS", "").split(",")
CSRF_TRUSTED_ORIGINS = []
CSRF_TRUSTED_ORIGINS += environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")


# Application

ASGI_APPLICATION = "app.asgi.application"
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.staticfiles",
    "app",
    "files",
    "inquiries",
    "posts",
]
APPEND_SLASH = False
REMOVE_SLASH = True
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "app.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": environ.get("RDS_HOSTNAME"),
        "PORT": environ.get("RDS_PORT"),
        "NAME": environ.get("RDS_DB_NAME"),
        "USER": environ.get("RDS_USERNAME"),
        "PASSWORD": environ.get("RDS_PASSWORD"),
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Internationalization

LANGUAGE_CODE = "en"
LANGUAGES = [("en", "English")]
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATICFILES_LOCATION = "static"
STATICFILES_DIRS = [join(BASE_DIR, "static")]
STATIC_ROOT = join(BASE_DIR, "public/static")
STATIC_URL = "/static/"
MEDIA_ROOT = join(BASE_DIR, "public/media")
MEDIA_URL = "/media/"
