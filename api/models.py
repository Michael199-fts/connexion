from django.db import models

class Participant(models.Model):
    male = 'ML'
    female = 'FL'
    SEX_CHOICES = [
        (male, 'male'),
        (female, 'female')
    ]
    photo = \
        models.ImageField(upload_to='photos/')
    first_name = \
        models.CharField(max_length=30)
    last_name = \
        models.CharField(max_length=30)
    email = \
        models.EmailField()
    sex = \
        models.CharField(max_length=2, choices=SEX_CHOICES)
