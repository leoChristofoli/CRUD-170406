from __future__ import absolute_import, unicode_literals

from .base import *

print('dev.settings')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = "9ghl@-+ocq7b--s-jmrh3b-$rvj57a5=t)v1-i64s0be*$--_1"
