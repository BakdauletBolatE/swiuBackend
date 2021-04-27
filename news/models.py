from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class PostCategories(models.Model):

    name = models.CharField('Имя категорий',max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Заголовок поста',max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField('Контентная часть', null=True, blank=True)
    category = models.ForeignKey(PostCategories,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
    created_at = models.DateTimeField('Время',default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"

class Like(models.Model):
    post = models.ForeignKey(Post,related_name="likes",  on_delete=models.CASCADE)
    user = models.CharField(max_length=255)

    

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = "Лайки"



class PostImages(models.Model):
    img = models.ImageField('Изображения',upload_to='Posts/Images')
    post = models.ForeignKey(Post,related_name="post_img", on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Фотография поста'
        verbose_name_plural = "Фотографий поста"

class PostComments(models.Model):
    description = models.TextField('Описание')
    post = models.ForeignKey(Post,related_name='post_com',on_delete=models.CASCADE)
    author = models.CharField('Автор',max_length=255)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Коментарий поста'
        verbose_name_plural = "Коментарий поста"

class Quote(models.Model):

    title = models.CharField('Название цитаты',max_length=255)
    description = models.TextField('Описание цитаты')
    author = models.CharField('Автор Цитаты',max_length=255)
    img = models.ImageField('изо',upload_to='Quete/Posters/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = "Цитаты"

class Questions(models.Model):

    title = models.CharField('Заголовок вопроса',max_length=255)
    description = models.TextField('Описание вопроса')
    img = models.ImageField('изо',upload_to='Questions/Posters/',blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = "Вопросы"

class PageHit(models.Model):
    url = models.CharField(max_length=255,unique=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.count

    class Meta:
        verbose_name = 'Просмотры страницы'
        verbose_name_plural = "Просмотры страницы"

class Request(models.Model):

    name = models.CharField('Ваше имя',max_length=255)
    email = models.EmailField('Ваш email')


    def __str__(self):
        return f'{self.name} | {self.email}'

    class Meta:

        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'




class Slides(models.Model):

    subTitle = models.CharField(max_length=255,verbose_name="Субтитл")
    title = models.CharField(max_length=255,verbose_name="Загаловка")
    btn = models.CharField(max_length=255,verbose_name="Названия первой кнопки")
    btn2 = models.CharField(max_length=255,verbose_name="Названия второй кнопки")
    link1 = models.CharField(max_length=255,verbose_name="первая ссылка")
    link2 = models.CharField(max_length=255,verbose_name="вторая ссылка")
    img = models.ImageField(upload_to="Slides/")

    class Meta:

        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
