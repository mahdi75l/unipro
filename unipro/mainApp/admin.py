from django.contrib import admin
# Register your models here.
from mainApp.models import Guid, CategoryGuid

admin.site.register(Guid)
admin.site.register(CategoryGuid)
