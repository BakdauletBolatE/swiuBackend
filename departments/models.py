from django.db import models
from faculties.models import Facult,Page



# Create your models here.

class Department(models.Model):
    name = models.CharField('Название кафедры',max_length=255)
    slug = models.SlugField('Url факультета',unique=True)
    description = models.TextField('Описание кафедра',blank=True,null=True)
    facult = models.ForeignKey(Facult,on_delete=models.CASCADE,related_name="departements")
    img = models.ImageField('Изображения', upload_to="Department/Posters/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"


class EducationalProgramsCat(models.Model):
    name = models.CharField('Название Категорий',max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория оброзовательных программам"
        verbose_name_plural = "Категорий оброзовательных программам"

class EducationalPrograms(models.Model):
    name = models.CharField('Название кафедры',max_length=255)
    slug = models.SlugField('Url факультета',unique=True)
    cat = models.ForeignKey(EducationalProgramsCat,on_delete=models.CASCADE)
    description = models.TextField('Описание кафедра',blank=True,null=True)
    img = models.ImageField('Изображения', upload_to="Edu/Posters/")
    facult = models.ForeignKey(Facult,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="edupros")
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Оброзовательные программа"
        verbose_name_plural = "Оброзовательные программы"

class ActivityDepartmentCat(models.Model):
    name = models.CharField('Заголовк категорий',max_length=255)
    slug = models.SlugField('Url категорий',unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория деятельности кафедра"
        verbose_name_plural = "Категория деятельности кафедры"

class ActivityDepartment(models.Model):
    title = models.CharField('Заголовок поста',max_length=255,null=True,blank=True)
    slug = models.SlugField('Url факультета',unique=True)
    short_description = models.TextField('Краткое описание')
    description = models.TextField('Полная описание',blank=True,null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    category = models.ForeignKey(ActivityDepartmentCat,on_delete=models.CASCADE)

    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Деятельность кафедра"
        verbose_name_plural = "Деятельность кафедры"



class ActivityDepartmentFoto(models.Model):
    photo = models.ImageField('Изображения',upload_to='Department/Activity/')
    department = models.ForeignKey(ActivityDepartment, related_name='activityDepartmentFoto', on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Деятельность кафедры фото"
        verbose_name_plural = "Деятельность кафедры фотки"