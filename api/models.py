from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    username = \
        models.CharField(max_length=150, unique=True, verbose_name='никнэйм')
    latitude = \
        models.CharField(max_length=15, unique=False, default=55.4507, verbose_name='широта')
    longitude = \
        models.CharField(max_length=15, unique=False, default=37.3656, verbose_name='долгота')

@receiver(post_save, sender=Participant)
def make_watermark(sender, instance=None, created=None, **kwargs):
    update_fields = kwargs.get('update_fields')
    if not update_fields:
        update_fields = frozenset()
    if created or 'photo' in update_fields:
        avatar = Image.open(instance.photo)
        draw = ImageDraw.Draw(avatar)
        font = ImageFont.truetype('api/Graphik-Regular-Web.ttf', size=150)
        draw.text((40, 40), 'connexionWM', font=font)
        new_image_io = BytesIO()
        avatar.save(new_image_io, format='PNG')

        temp_name = f"{instance.photo.name}"
        instance.photo.save(
            temp_name,
            content=ContentFile(new_image_io.getvalue()),
            save=False
        )
        instance.save()

class Sympaty(models.Model):
    class Meta:
        verbose_name = 'Симпатия'
        verbose_name_plural = 'Симпатии'

    sender = \
        models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name='пользователь',
                          related_name='sender')
    addressee = \
        models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name='объект симпатии',
                          related_name='addressee')