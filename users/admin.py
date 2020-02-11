from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
# po każdym makemigration trzeba model/baz zarejestrować tutuaj
