from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Milestone

# Register Milestone model to show in admin interface
admin.site.register(Milestone)
