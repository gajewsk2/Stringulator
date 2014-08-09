import os

ROOT_PATH = os.path.dirname(__file__)

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('micah', 'micahbgaj@gmail.com'),
)

MANAGERS = ADMINS

import dj_database_url

if DEBUG:
    DATABASE_URL = 'postgres://localhost/storage'
else:
    DATABASE_URL = 'postgres://hxtnsxsmxkrgor:H5vYN7g2Nn0ZQCmWZeGiUzLvMC@ec2-54-204-21-178.compute-1.amazonaws.com:5432/dk5va592r6j0v'
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.stringulator.com', 'stringulator.com',
                 'micahgajewski.com', 'www.micahgajewski.com', 'stringulator.herokuapp.com', 'localhost', '127.0.0.1']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
# if DEBUG:
# PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
# MEDIA_URL = os.path.join(PROJECT_PATH, '../static/')
# else:
# MEDIA_URL = 'https://rawgithub.com/Matthew-L/GTC-Web/master/static/'
# MEDIA_URL = 'http://mattlodes.com/static/'
MEDIA_URL = '/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# Static asset configuration
# import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

if DEBUG:
    STATIC_URL = '/static/'
else:
    STATIC_URL = 'https://s3.amazonaws.com/stringulator-production/static/'

STATIC_ROOT = os.path.abspath('static')
COMPRESS_ROOT = os.path.abspath('static')

STATICFILES_DIRS = (
    os.path.abspath('stringulator\\static'),
    # os.path.abspath('dist'),
)

# Additional locations of static files
# STATICFILES_DIRS = (
# [os.path.join(ROOT_PATH, 'static')]
#    ('assets', 'static'),
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*gis)!8a&uptme_abhztm8o#c)n%v%euqs2&%!zaym7anjc^0*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'stringulator.redirect.redirect_middleware.WWWRedirectMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stringulator.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'stringulator.wsgi.application'

# TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '../../../../../..////', 'templates').replace('\\','/'),
#                  os.path.join(os.path.dirname(__file__), '../../../../../..////', 'article/templates').replace('\\', '/'),)



BASE_DIR = os.path.abspath('stringulator/templates')

TEMPLATE_DIRS = (
    BASE_DIR,
    BASE_DIR + '/calculator',
    BASE_DIR + '/contact',
    BASE_DIR + '/homepage',
    BASE_DIR + '/search',
    BASE_DIR + '/users',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "compressor",
    'django.contrib.admin',
    'users',
    'calculator',
    'calculator.guitarstring',
    'stringulator',
    'stringulator.templatetags',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

INTERNAL_IPS = ("request.META['REMOTE_ADDR']", )

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'stringulator.context_processor.debug',
)