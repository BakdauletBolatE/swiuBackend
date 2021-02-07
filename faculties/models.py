from django.db import models

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




