from django.test import TestCase

# Create your tests here.
from django.shortcuts import reverse

from ..models import BazaarObject
from users.models import User


class BazaarObjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='+1234567890123',
                                             slug='1234567890123',
                                             password='happybirthday',
                                             locale='unn')
        self.object_ = BazaarObject.objects.create(name='Gucci bag',
                                                   description='akpa',
                                                   category='bag',
                                                   classification='item',
                                                   owner=self.user, ask_price=2000,
                                                   )

    def test_object_data(self):
        user = User.objects.get(pk=self.object_.pk)
        object_ = BazaarObject.objects.get(pk=self.object_.pk)
        self.assertEqual(user, object_.owner)
        self.assertEqual(str(user.username), '+1234567890123')
        self.assertEqual(str(object_.name), 'Gucci bag')
        self.assertEqual(int(object_.ask_price), 2000)

    def test_get_absolute_url(self):
        self.assertEqual(self.object_.get_absolute_url(),
                         reverse('%s:details' % self.object_.classification,
                                 kwargs={'pk': self.object_.pk},)
                         )
