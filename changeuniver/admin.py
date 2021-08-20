from django.contrib import admin
from .models import Zayavka, Shifr


class ZayavkaAdmin(admin.ModelAdmin):
    readonly_fields = ('genereted_file',)

admin.site.register(Zayavka, ZayavkaAdmin)
admin.site.register(Shifr)

