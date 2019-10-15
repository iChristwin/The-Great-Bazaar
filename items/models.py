from django.db import models

# Create your models here.
# My imports -----------------------------------------------------------------
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from cloudinary.models import CloudinaryField


from .constants import CATEGORIES
# =======================================================================


def front_photo_path(instance, filename):
    return '/'.join(['item', str(instance.pk), 'front-'+str(filename)])


def back_photo_path(instance, filename):
    return '/'.join(['item', str(instance.pk), 'back-'+str(filename)])


class Item(models.Model):
    """
    Core model for the Bazaar platform. It represents the value-unit
    exchanged on the platform.
    """
    name = models.CharField(max_length=100,)
    description = models.TextField(default='', blank=True)
    available = models.BooleanField(default=True, blank=True)
    category = models.CharField(max_length=25, choices=CATEGORIES)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )

    photo_front = CloudinaryField('image', default='https://res.cloudinary.com/ichristwin/image/upload/v1571126185/wmbalgw9rof6jen0ni5q.png')
    photo_back = CloudinaryField('image', default='https://res.cloudinary.com/ichristwin/image/upload/v1571126185/wmbalgw9rof6jen0ni5q.png')

    booked_for = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                   related_name='%(class)s_booked_for',
                                   verbose_name='Booked for',
                                   null=True, blank=True, )
    date_added = models.DateTimeField(auto_now_add=True, blank=True,)
    last_modified = models.DateTimeField(auto_now=True, blank=True,)
    owner_confirmation = models.BooleanField(default=False)
    buyer_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return "%(category)s: %(name)s" % ({'category': self.category,
                                            'name': self.name})

    def get_absolute_url(self):
        return reverse('item:details', kwargs={'pk': self.pk})

    def get_return_url(self):
        return reverse('item:inventory')

    def get_description(self):
        return self.description.strip().split('**')


# =======================================================================
