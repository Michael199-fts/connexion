from django.db import models
from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
    male = 'ML'
    female = 'FL'
    SEX_CHOICES = [
        (male, 'мужской'),
        (female, 'женский')
    ]
    photo = \
        models.ImageField(upload_to='photos/', verbose_name='аватар')
    first_name = \
        models.CharField(max_length=30, verbose_name='имя')
    last_name = \
        models.CharField(max_length=30, verbose_name='фамилия')
    email = \
        models.EmailField(null=True)
    sex = \
        models.CharField(max_length=2, choices=SEX_CHOICES, verbose_name='пол')
