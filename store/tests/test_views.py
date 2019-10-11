from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from django.shortcuts import redirect

from ..models import BazaarObject
from users.models import User

from ..views import add_item, edit_item, item_inventory
from ..views import add_lodge, update_lodge, lodge_inventory
from ..views import create_job, update_job, job_list
from ..views import like_object, dislike_object, object_details

from commons.views import home

# class-based views (esp. generic) omitted in testing
# [...There's reason to believe they are stable, jst make sure they run]


def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


class TestViews(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
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
        self.lodge = BazaarObject.objects.create(name='Green House',
                                                 description='1 bedroom, kitchen, bathroom, '
                                                             'adequately furnished',
                                                 category='flat',
                                                 classification='lodge',
                                                 owner=self.user, ask_price=7000,
                                                 )
        self.skill = BazaarObject.objects.create(category='cook', owner=self.user,
                                                 description="I'm a well refined Cook, "
                                                             "main prepares Rice, Soup, Stew, "
                                                             "any Quantity of choice",
                                                 classification='skill', )

    def test_add_item_view(self):
        request = self.request_factory.get(redirect('item:add'))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = add_item(request)
        self.assertContains(response, 'Add')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    def test_edit_item_view(self):
        request = self.request_factory.get(redirect('item:update', self.object_.pk))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = edit_item(request, self.object_.pk)
        self.assertContains(response, 'Edit')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    def test_item_inventory_view(self):
        request = self.request_factory.get(redirect('item:inventory',))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = item_inventory(request)
        self.assertContains(response, 'Inventory')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    # ================================================

    def test_add_lodge_view(self):
        request = self.request_factory.get(redirect('lodge:add'))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = add_lodge(request)
        self.assertContains(response, 'Add')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    def test_update_lodge_view(self):
        request = self.request_factory.get(redirect('lodge:update', self.lodge.pk))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = update_job(request, self.lodge.pk)
        self.assertContains(response, 'Edit')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    def test_lodge_inventory_view(self):
        request = self.request_factory.get(redirect('lodge:inventory',))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = lodge_inventory(request)
        self.assertContains(response, 'Inventory')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    # ================================================

    def test_create_job_view(self):
        request = self.request_factory.get(redirect('job:create'))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = create_job(request)
        self.assertContains(response, 'Add')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    def test_update_job_view(self):
        request = self.request_factory.get(redirect('job:update', self.skill.pk))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = update_job(request, self.object_.pk)
        self.assertContains(response, 'Edit')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    def test_job_list_view(self):
        request = self.request_factory.get(redirect('job:inventory',))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = job_list(request)
        self.assertContains(response, 'Inventory')
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    # ================================================

    def test_object_details_view(self):
        request = self.request_factory.get(redirect('item:details', self.object_.pk))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = object_details(request, self.object_.pk)
        self.assertContains(response, self.object_.name)
        self.assertEqual(response.status_code, 200)
        # status code 200 == OK 

    def test_like_object_view(self):
        request = self.request_factory.get(redirect('item:like', self.object_.pk))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = like_object(request, self.object_.pk)
        self.assertEqual(response.status_code, 302)
        # status code 302 == FOUND

    def test_dislike_object_view(self):
        request = self.request_factory.get(redirect('item:dislike', self.object_.pk))

        request.user = self.user
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()

        response = dislike_object(request, self.object_.pk)
        self.assertEqual(response.status_code, 302)
        # status code 302 == FOUND
