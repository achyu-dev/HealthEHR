from django.contrib import admin

# Register your models here.

from .models import User, UploadedFile

admin.site.register(User)
admin.site.register(UploadedFile)
