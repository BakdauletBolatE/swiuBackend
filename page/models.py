from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from faculties.models import Page
import random


class Widget(models.Model):

    widgettype = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,related_name="page")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    page = models.ForeignKey(Page,on_delete=models.CASCADE,related_name="widgets")
    order = models.PositiveBigIntegerField(default=0)
    iic_id = models.CharField(max_length=255, null=True,blank=True)

    def save(self, *args, **kwargs):
        randomIIC = f'#{self.id}' + ''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)])
        self.iic_id = randomIIC
        super().save(*args, **kwargs)  # Call the "real" save() method.
        

    def __str__(self):
        return str(self.id)


class WidgetText(models.Model):

    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

class WidgetOnlyText(models.Model):

    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

class WidgetPhoto(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="Images/",blank=True,null=True)

class WidgetGalery(models.Model):

    title = models.CharField(max_length=255,blank=True,null=True)


class WidgetGalleryPhotos(models.Model):

    image = models.ImageField(upload_to="Images/",blank=True,null=True)
    widgetGalery = models.ForeignKey(WidgetGalery,on_delete=models.CASCADE ,related_name="images")