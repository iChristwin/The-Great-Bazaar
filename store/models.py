from django.db import models

# Create your models here.
# My imports -----------------------------------------------------------------
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

import cloudinary
from cloudinary.models import CloudinaryField

from django.dispatch import receiver
from django.db.models.signals import pre_delete

from .constants import CATEGORIES
# =======================================================================

DOMAIN = getattr(settings, 'DOMAIN', 'localhost')


def front_photo_path(instance, filename):
    return '/'.join(['item', str(instance.pk), 'front-'+str(filename)])


def back_photo_path(instance, filename):
    return '/'.join(['item', str(instance.pk), 'back-'+str(filename)])

# =======================================================================


class Store(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, )
    is_verified = models.BooleanField(default=False, blank=True)

    def get_absolute_url(self):
        return reverse("store:details", kwargs={'pk': self.pk})

    def get_direct_url(self):
        return DOMAIN+reverse("store:details", kwargs={'pk': self.pk})


class Stock(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField(default='', blank=True)
    price = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=25, choices=CATEGORIES)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, )
    quantity = models.PositiveSmallIntegerField(default=2)

    date_added = models.DateTimeField(auto_now_add=True, blank=True,)
    orders = models.ManyToManyField(get_user_model(), related_name='orders', )

    def __str__(self):
        return "%(category)s: %(name)s" % ({'category': self.category,
                                            'name': self.name})

    def get_absolute_url(self):
        return reverse('stock:details', kwargs={'pk': self.pk})

    def get_return_url(self):
        return reverse('stock', kwargs={'pk': self.store.pk})

    def get_description(self):
        return self.description.strip().split('**')

    def get_direct_url(self):
        return DOMAIN+reverse("stock:details", kwargs={'pk': self.pk})


class CloudinaryPhoto(models.Model):
    image = CloudinaryField('image')
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE, )


@receiver(pre_delete, sender=CloudinaryPhoto)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)

