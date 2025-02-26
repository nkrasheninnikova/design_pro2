from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    patronymic = models.CharField(max_length=100, blank=True)


class Avatar(models.Model):
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    username = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', blank=False)

    def __str__(self):
        return self.name


class Request(models.Model):
    STATUS_CHOICES = [
        ('Н', 'Новая'),
        ('П', 'Принято в работу'),
        ('В', 'Выполнено')
    ]

    name = models.CharField(max_length=100, verbose_name='Заголовок', blank=False)
    date = models.DateTimeField(verbose_name='Временная метка', auto_now_add=True)
    description = models.TextField(max_length=254, verbose_name='Описание', blank=False)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', verbose_name='План помещения')
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICES, default='Н')
    user = models.ForeignKey('UserProfile', verbose_name='Пользователь', on_delete=models.CASCADE)
    image_done = models.ImageField(upload_to='image_done/', verbose_name='Готовое изображение', blank=True)
    comment = models.TextField(max_length=254, verbose_name='Комментарий', blank=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.name