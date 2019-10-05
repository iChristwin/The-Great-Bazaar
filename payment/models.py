from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

from interest.models import Offer
from .constants import BANKS

# ============================================================================


class Collect(models.Model):
    amount = models.FloatField(null=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, )
    date = models.DateField(null=True)
    received = models.BooleanField(default=False)
    trnx_id = models.CharField(max_length=255, default='')
    contract = models.OneToOneField(Offer, on_delete=models.PROTECT, )

    class Meta:
        abstract = True

# ============================================================================


class CollectDeposit(Collect):
    acc_name = models.CharField(max_length=255, default='')
    acc_number = models.IntegerField(null=True)
    bank = models.CharField(max_length=60, choices=BANKS, default='')


# ============================================================================


class XYZPay(Collect):
    acc_id = models.IntegerField()

    class Meta:
        abstract = True


# ============================================================================


class Accounts(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(null=True)
    bank = models.CharField(max_length=60, choices=BANKS)
    ok = models.BooleanField(default=True)

# ============================================================================


class Disburse(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, )
    disbursed = models.BooleanField(default=False)
    editable = models.BooleanField(default=True)
    contract = models.OneToOneField(Offer, on_delete=models.PROTECT, )

    class Meta:
        abstract = True


class DisburseDeposit(Disburse):
    acc_name = models.CharField(max_length=255, default='')
    acc_number = models.IntegerField(null=True)
    bank = models.CharField(max_length=60, choices=BANKS, default='')
