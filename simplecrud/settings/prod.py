from __future__ import absolute_import, unicode_literals
import dj_database_url
import os

from .base import *
print('Prod Settings')

try:
    DEBUG = os.environ['DEBUG']
except:
    DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
INSTALLED_APPS += ("gunicorn", "storages")

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['*']

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_HOST = os.environ['AWS_S3_HOST']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s.s3.amazonaws.com/" % os.environ['AWS_STORAGE_BUCKET_NAME']
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = "simplecrud.s3utils.StaticS3BotoStorage"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'