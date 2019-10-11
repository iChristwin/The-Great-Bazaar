from django.db import models

# Create your models here.
# My imports ------------------------------------------------------------
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from items.models import Item
from store.models import Stock

# =======================================================================


class Bookmarks(models.Model):
    bookmarked = models.ManyToManyField(Item, )
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                 blank=True,)

    class Meta:
        verbose_name_plural = 'Bookmarks'

    def __str__(self):
        return "%(owner)s bookmarks" % ({'owner': self.owner, })

    def get_absolute_url(self):
        return reverse("bookmark:details", kwargs={'pk': self.pk})

# =======================================================================


class Order(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,
                                 blank=True,)
    quantity = models.PositiveSmallIntegerField(default=1)
    accepted = models.BooleanField(default=False)
    order_time = models.DateTimeField(auto_now_add=True, blank=True,)

    def __str__(self):
        return "%(stock)s order" % ({'stock': self.stock, })

    def get_absolute_url(self):
        return reverse("stock:details", kwargs={'pk': self.stock.pk})

# =======================================================================


class Offer(models.Model):
    offer = models.FloatField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              verbose_name="Bidder", blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True,)
    accepted = models.BooleanField(default=False)

    # users should be able to express interest to an item using this.
    # to place an offer. should be deletable, editable and acceptable
    # except accepted, offers can be edited, to edit cancel acceptance

    def __str__(self):
        return "%(user)s interested in %(subject)s" % ({'user': self.owner,
                                                        'subject': self.item.name})

    def get_absolute_url(self):
        return reverse("item:details", kwargs={'pk': self.item.pk})

# =======================================================================


class Bargain(models.Model):
    bargain = models.FloatField()
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name="Seller", blank=True,)
    last_modified = models.DateTimeField(auto_now=True, blank=True,)

    def get_absolute_url(self):
        return reverse("item:details", kwargs={'pk': self.offer.item.pk})

# =======================================================================
