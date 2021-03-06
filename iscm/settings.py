"""
Django settings for iscm project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
FIELD_ENCRYPTION_KEY = '9HvoULGJ4lSkGECI2TmMTYEVkNhXF0cAJXBINrkYi08='
SECRET_KEY = '@=kb&5((d_#47szs7r^wamq!)s3=am6i_^6$r#ipr%kns-gt1s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
'localhost:4200',
'localhost:3400',
'localhost:8000',
)
                                                                        

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'oauth2_provider',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'location.apps.LocationConfig',
    'account',
    'contract',
    'api',
    'rest_framework_swagger',
    'django_filters',
    'django_cleanup',
    'corsheaders',
    'encrypted_model_fields',
    'security',
    # 'microsoft_auth',

]

MIDDLEWARE = [
    'iscm.middleware.RemoveHeaders',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'security.middleware.DoNotTrackMiddleware',
    'security.middleware.ContentNoSniff',
    'security.middleware.XssProtectMiddleware',
    'security.middleware.XFrameOptionsMiddleware',
    # 'iscm.middleware.CustomMiddleware',
]


CORS_ALLOW_HEADERS = (
    'Authenticate',
    'userId',
    'authToken',
    'apptoken',
    'appid',
    'accept',
    'devicetype',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Access-Control-Allow-Headers',
)
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.DjangoModelPermissions',
#     )
# }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        )

}

REST_FRAMEWORK = {    
    'DEFAULT_PERMISSION_CLASSES': (
        'contract.permissions.DisableOptionsPermission',
        'account.permissions.DisableOptionsPermission',
        'location.permissions.DisableOptionsPermission',
    )
}

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
#     ),
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.TokenAuthentication',
#    ),
#    'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAdminUser',
#    ),
#    'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }



# OAUTH2_PROVIDER = {
#     # this is the list of available scopes
#     'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
# }

ROOT_URLCONF = 'iscm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'iscm/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
    # {
        # other template settings...
        # 'OPTIONS': {
            # 'context_processors': [
                # other context_processors...
                # 'microsoft_auth.context_processors.microsoft',
            # ],
        # },
    # },
]

WSGI_APPLICATION = 'iscm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iscm_pilot',
        # 'NAME': 'pilot_iscm1',
        # 'USER': 'developer',
        'USER': 'root',
        # 'PASSWORD': 'pass,123',
        'PASSWORD': 'rootgivenpassword',
        # 'HOST': '13.235.195.93',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# http://10.175.2.29:3400/



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# AUTHENTICATION_BACKENDS = [
    # 'microsoft_auth.backends.MicrosoftAuthenticationBackend',
    # 'django.contrib.auth.backends.ModelBackend' # if you also want to use Django's authentication
    # I recommend keeping this with at least one database superuser in case of unable to use others
# ]


# values you got from step 2 from your Mirosoft app
# MICROSOFT_AUTH_CLIENT_ID = 'f3bd2cf0-1ab6-4686-af39-d8afdc3684d0'
# MICROSOFT_AUTH_CLIENT_SECRET = 'your-client-secret-from-apps.dev.microsoft.com'

# pick one MICROSOFT_AUTH_LOGIN_TYPE value
# Microsoft authentication
# include Microsoft Accounts, Office 365 Enterpirse and Azure AD accounts
# MICROSOFT_AUTH_LOGIN_TYPE = 'ma'

# Xbox Live authentication
# MICROSOFT_AUTH_LOGIN_TYPE = 'xbl'  # Xbox Live authentication


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# LOGIN_REDIRECT_URL='/'

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL="/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'iscmproject001@gmail.com'
EMAIL_HOST_PASSWORD = 'iscm1234'
EMAIL_PORT = 587


strOpplink = "http://103.81.89.7/cashAPI/api/APIOpportunityDetails?Opp_id={0}&ApiKey=superapi00000"
# strOpplink = "http://172.32.1.180/cashAPI/api/APIOpportunityDetails?Opp_id={0}&ApiKey=superapi00000"
