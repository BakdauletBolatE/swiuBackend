from django.db import models
from departments.models import Department,EducationalPrograms
from faculties.models import Facult

# Create your models here.
class Position(models.Model):

    name = models.CharField('Должность персонала',max_length=255)
    slug = models.SlugField('Url Должность персонала',unique=True)

    class Meta:
        verbose_name = 'Должность персонала'
        verbose_name_plural = 'Должность персоналов'
        
    def __str__(self):
        return self.name

class StaffCat(models.Model):

    name = models.CharField('Категория персонала',max_length=255)
    slug = models.SlugField('Url Категория персонала',unique=True)

    class Meta:
        verbose_name = 'Категория персонала'
        verbose_name_plural = 'Категорий персонала'
        
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField('Имя персонала',max_length=255)
    slug = models.SlugField('Url персонала',unique=True)
    img = models.ImageField('Изоброжения персонала', upload_to="Staff/Posters")
    position = models.ForeignKey(Position,on_delete=models.CASCADE,blank=True,null=True)
    staffCat = models.ForeignKey(StaffCat,on_delete=models.CASCADE,blank=True,null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    educationalPrograms = models.ManyToManyField(EducationalPrograms,null=True)
    email = models.EmailField('Почта персонала',blank=True,null=True,max_length=255)
    adress = models.CharField('Адрес персонала',blank=True,null=True,max_length=255)
    phone = models.CharField('Телефон персонала',blank=True,null=True,max_length=255)
    facult = models.ForeignKey(Facult,on_delete=models.CASCADE)
    about = models.TextField('О персонале')

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонали'

    def __str__(self):
        return self.name
