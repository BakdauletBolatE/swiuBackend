from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.




class Post(models.Model):
    title = models.CharField('Заголовок поста',max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField('Описание поста')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
    created_at = models.DateTimeField('Время',default=datetime.now())

class Like(models.Model):
    post = models.ForeignKey(Post,related_name="likes",  on_delete=models.CASCADE)
    user = models.CharField(max_length=255)



class PostImages(models.Model):
    img = models.ImageField('Изображения',upload_to='Posts/Images')
    post = models.ForeignKey(Post,related_name="post_img", on_delete=models.CASCADE,default=0)

class PostComments(models.Model):
    description = models.TextField('Описание')
    post = models.ForeignKey(Post,related_name='post_com',on_delete=models.CASCADE)
    author = models.CharField('Автор',max_length=255)

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

class PageHit(models.Model):
    url = models.CharField(max_length=255,unique=True)
    count = models.PositiveIntegerField(default=0)
    