from django.contrib import admin
from .models import Codes_load


class CodesAdmin(admin.ModelAdmin):
    list_display = ['prod', 'passFile', 'loadDate']


admin.site.register(Codes_load, CodesAdmin)
