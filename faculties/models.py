from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Facult(models.Model):
    name = models.CharField('Название факультета',max_length=255)
    slug = models.SlugField('Url факультета',unique=True)
    description = models.TextField('Описание факультета',blank=True,null=True)
    photo = models.ImageField('Изображения',upload_to='Facult/Posters/',default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


class PageCategory(models.Model):
    name = models.CharField('НАзвани катоегрий',max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория Страницы"
        verbose_name_plural = "Категорий Страницы"


class Page(models.Model):

    order = models.IntegerField('Филтрация',default=0)
    title = models.CharField('Название страницы',max_length=255)
    url = models.CharField('Ссылка НУЖНО ИМЯ',max_length=255)
    slug = models.SlugField('slug это обычный слаг',null=True,blank=True)
    link = models.CharField('Ссылку на сайт',null=True,blank=True,default=None,max_length=255)
    content = RichTextUploadingField('Контентная часть',null=True,blank=True)
    img = models.ImageField('Постер страницы',upload_to="Page/",blank=True,null=True)
    category = models.ForeignKey(PageCategory,related_name='page',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class PageImages(models.Model):

    page = models.ForeignKey(Page,on_delete=models.CASCADE,related_name="pageImages")
    img = models.ImageField('Фотографий страницы',upload_to="PageImages/")

    class Meta:
        verbose_name = "Фотограция страницы"
        verbose_name_plural = "Фотограций страницы"





