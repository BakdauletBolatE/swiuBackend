from django.db import models

# Create your models here.

class Quote(models.Model):

    title = models.CharField('Название цитаты',max_length=255)
    description = models.TextField('Описание цитаты')
    author = models.CharField('Автор Цитаты',max_length=255)
    img = models.ImageField('изо',upload_to='Quete/Posters/')

    def __str__(self):
        return self.title

class Questions(models.Model):

    title = models.CharField('Заголовок вопроса',max_length=255)
    description = models.TextField('Описание вопроса')
    img = models.ImageField('изо',upload_to='Questions/Posters/',blank=True,null=True)

    def __str__(self):
        return self.title