from django.db import models
from docxtpl import DocxTemplate
from django.conf import settings
import datetime
from departments.models import EducationalPrograms


class Shifr(models.Model):
    name = models.CharField('Мамандық шифры, атауы', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Шифр"
        verbose_name_plural = "Шифры"       

class Zayavka(models.Model):

    rejim = (
        ('Қашықтан', 'Қашықтан'),
        ('Күндізгі', 'Күндізгі')
    )

    lang = (
        ('Қазақ', 'Қазақ'),
        ('Орыс', 'Орыс')
    )

    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Отчество', max_length=255)
    shifr_name = models.ForeignKey(EducationalPrograms, on_delete=models.CASCADE, verbose_name='Мамандық шифры, атауы')
    course = models.SmallIntegerField('Курс',max_length=4, default=1)
    top = models.CharField('Топ', max_length=12)
    phone = models.CharField('Тел номері', max_length=11)
    rejim = models.CharField('Оқу режимы', max_length=255, choices=rejim)
    language = models.CharField('Оқу тілі', max_length=255, choices=lang)
    genereted_file = models.FileField(upload_to="genereted/", null=True, blank=True)

    def save(self, *args, **kwargs):
        doc = DocxTemplate("template_form.docx")
        month = datetime.date.today().month
        day = datetime.date.today().day
        year = datetime.date.today().year
        
        context = {
            'fio': f'{self.surname} {self.name} {self.last_name}',
            'name': self.name,
            'shifr_name': self.shifr_name,
            'course': self.course,
            'top': self.top,
            'phone': self.phone,
            'rejim': self.rejim,
            'language': self.language,
            'month': month,
            'day': day,
            'year': year
        }
        doc.render(context)
        name = f"/genereted/{self.name}_{self.surname}_request.docx"
        print(settings.MEDIA_ROOT)
        doc.save(str(settings.MEDIA_ROOT) + name)
        self.genereted_file = name
        super(Zayavka, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Заявку"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'{self.surname} {self.name}'


