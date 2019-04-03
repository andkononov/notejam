#!/usr/bin/python

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.docker")
django.setup()

from django.contrib.auth import get_user_model
from django.db import IntegrityError
try:
    get_user_model().objects.create_superuser(
        username='admin@notejam',
        password='hei9cheM',
        email='admin@notejam.int',
    )
except IntegrityError:
    pass
else:
    print('Super user has been created')