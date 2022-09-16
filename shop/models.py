from django.db import models
import uuid
from django.urls import reverse


# Create your models here.

class Shop(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=100, verbose_name="Name of clothes")
    clothes_image = models.ImageField(upload_to='clothes_media/', blank=True, verbose_name="Clothes photo")
    info = models.TextField(max_length=1000, blank=True, verbose_name='info_about_clothes')
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, verbose_name='Price')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clothes_detail', kwargs={'pk': str(self.pk)})
