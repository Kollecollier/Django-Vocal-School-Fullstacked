"Project Admin file"
from django.contrib import admin
from .models import Appointment, photos

admin.site.register(Appointment)
admin.site.register(photos)
