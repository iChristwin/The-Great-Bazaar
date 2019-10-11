from django.db import models

# Create your models here.
# My imports -----------------------------------------------------------------
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .constants import VIEWS, GENDER
from .validators import is_mobile, is_sluggy, is_enlisted


DOMAIN = getattr(settings, 'DOMAIN', 'localhost')


class User(AbstractUser):
    """
    Custom user model for project. with focus on students, includes
    locale field subsets user into specific collage communities
    Reg.No could potentially verify ID

    """
    username = models.CharField(max_length=14, verbose_name='Mobile Number',
                                unique=True, validators=[is_mobile], )
    locale = models.CharField(max_length=50, validators=[is_enlisted],
                              default='', )
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default=GENDER[0][0])
    alias = models.SlugField(max_length=10, validators=[is_sluggy])
    # could be potentially be used to collect real user info
    view = models.CharField(max_length=10, default=VIEWS[0], )
    is_verified = models.BooleanField(default=False, blank=True)
    last_modified = models.DateField(auto_now=True, blank=True,)
    batch = models.CharField(blank=True, default='0', max_length=2)
    # review_count in review model is == sales_count

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return "%s" % self.username

    def get_absolute_url(self):
        return reverse("user:details", kwargs={'pk': self.pk})

    def get_home_url(self):
        return reverse("%s:home" % self.view)

    def get_search_url(self):
        return reverse("%s:search" % self.view)

    def get_referral(self):
        return DOMAIN+'/'+reverse('r_signup', kwargs={'locale': self.locale,
                                  'code': hex(int(self.username))[2:]
                                  })
