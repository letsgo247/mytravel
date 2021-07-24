from .base import *


# import environ
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
# # reading .env file
# environ.Env.read_env(
#     env_file= os.path.join(BASE_DIR, '.env')
# )


def read_secret(secret_file):
    file = open('/run/secrets/' + secret_file)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mariadb',
#         'USER': 'root',
#         'PASSWORD': 'password1234',
#         'HOST': 'mariadb_container',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/db.sqlite3',
    }
}

print(DATABASES)