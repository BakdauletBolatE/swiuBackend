from django.db import models
from departments.models import EducationalPrograms
from staff.models import Staff
# Create your models here.

class Year(models.Model):
    year = models.IntegerField(default=0,verbose_name="Год")
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to="Year/Posters/")

    def __str__(self):
        return f"Год :{self.year}"

    class Meta:
        verbose_name = 'Год для Библиотеки'
        verbose_name_plural = "Год для Библиотеки"


class Book(models.Model):

    name = models.CharField("Название книги",max_length=255)
    description = models.TextField("Описание книги")
    eduProgram = models.ForeignKey(EducationalPrograms,on_delete=models.CASCADE,null=True,blank=True)
    author = models.ForeignKey(Staff, on_delete=models.CASCADE,null=True,blank=True)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    poster = models.ImageField(upload_to="Book/Posters/",null=True,blank=True)
    img = models.ImageField(upload_to="Book/Posters/" ,null=True,blank=True)
    pdffile = models.FileField(upload_to="Book/Pdf",null=True,blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Книгу {self.name} сделали "

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = "Библиотеки"



