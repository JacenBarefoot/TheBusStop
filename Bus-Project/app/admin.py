from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Passenger)
admin.site.register(Tag)
admin.site.register(Arriving)