from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from .models import Today12

# Register your models here.
class Today12Resource(resources.ModelResource):

    class Meta:
        model = Today12
        field = ('-month', '-day')

class Today12Admin(ImportExportActionModelAdmin):
    resource_class = Today12Resource


admin.site.register(Today12, Today12Admin)