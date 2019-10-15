from django.dispatch import receiver
from django.db.models.signals import pre_delete

import cloudinary

from .models import Item


@receiver(pre_delete, sender=Item)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.photo_front.public_id)
    cloudinary.uploader.destroy(instance.photo_back.public_id)

