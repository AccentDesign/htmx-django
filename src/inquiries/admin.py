from django.contrib import admin

from . import models

admin.site.register(models.Inquiry, list_display=["created_at", "name", "email"])
