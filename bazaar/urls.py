"""bazaar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.views import static
from django.views.generic import TemplateView

from users.views import SignUpView
from users.views import JoinCommunity, RegistrationClosed
from commons.views import home

from search.views import BazaarSearch

urlpatterns = [
    path('', home, name='home'),
    path('welcome/', BazaarSearch.as_view(), name='welcome'),
    path('<locale>/signup/', SignUpView.as_view(), name='signup'),
    path('<locale>/referral/<code>/signup/', SignUpView.as_view(), name='r_signup'),

    path('', include('django.contrib.auth.urls')),
    path('search/', include('haystack.urls')),
    path('password/', include('users.url.password')),
    path('user/', include('users.urls', namespace='user')),
    path('item/', include('items.urls', namespace='item')),
    path('store/', include('store.urls.store', namespace='store')),
    path('stock/', include('store.urls.stock', namespace='stock')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('offer/', include('interest.urls.offer', namespace='offer')),
    path('bargain/', include('interest.urls.bargain', namespace='bargain')),
    path('bookmark/', include('interest.urls.bookmark', namespace='bookmark')),
    path('order/', include('interest.urls.order', namespace='order')),

    path('admin/', admin.site.urls),
    path('join/', JoinCommunity.as_view(), name='join'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('intro/', TemplateView.as_view(template_name='intro.html'), name='intro'),
    path('registration/closed/', RegistrationClosed.as_view(), name='closed'),

]

if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', static.serve,
                        {'document_root': settings.MEDIA_ROOT, }
                        ),
                    ]
