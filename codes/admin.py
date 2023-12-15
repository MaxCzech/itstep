from django.contrib import admin
from .models import Codes


class CodesAdmin(admin.ModelAdmin):
    list_display = ['id', 'prod', 'serialNum', 'code', 'loadDate', 'ignor', 'sold', 'soldDate', 'order']
    list_editable = ['ignor', 'sold']
    list_filter = ['prod', 'order', 'code']


admin.site.register(Codes, CodesAdmin)
