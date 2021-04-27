from page.models import Widget, WidgetGalery, WidgetGalleryPhotos, WidgetPhoto,WidgetText
from django.contrib import admin

# Register your models here.
admin.site.register(WidgetText)
admin.site.register(Widget)
admin.site.register(WidgetPhoto)
admin.site.register(WidgetGalleryPhotos)
admin.site.register(WidgetGalery)