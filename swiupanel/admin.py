from django.contrib import admin
from .models import Widget,WidgetType,WidgetItems
# Register your models here.
admin.site.register(Widget)
admin.site.register(WidgetItems)
admin.site.register(WidgetType)