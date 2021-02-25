from django.db import models
from faculties.models import Page
# Create your models here.

class WidgetType(models.Model):
    name = models.CharField('Название типа виджета?', max_length=255)

class Widget(models.Model):

    name = models.CharField('Название виджета',max_length=255, blank=True,null=True)
    widget_type = models.ForeignKey(WidgetType,related_name="widget",verbose_name="Тип виджета которому нужно подключиться",on_delete=models.CASCADE)
    page = models.ForeignKey(Page,related_name="widgets",verbose_name="Страница которому нужно подключиться",on_delete=models.CASCADE)

class WidgetItems(models.Model):

    title = models.CharField('Загаловок виджета',max_length=255,blank=True,null=True)
    widget_photo = models.ImageField('Фото для виджета', upload_to="WidgetImages/",blank=True,null=True)
    widget = models.ForeignKey(Widget,verbose_name="Виджет",related_name="widgetitems", on_delete=models.CASCADE)
    content = models.TextField('Контентная часть виджета',null=True,blank=True)

  
