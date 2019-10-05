from django.urls import path

# My imports -----------------------------------------------------------------
from ..views import accept_offer, cancel_offer
from ..views import UpdateOffer, DeleteOffer
from ..views import MyOffers


app_name = 'offer'
urlpatterns = [
    path('<int:pk>/accept/', accept_offer, name='accept'),
    path('<int:pk>/cancel/', cancel_offer, name='cancel'),
    path('<int:pk>/update/', UpdateOffer.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteOffer.as_view(), name='delete'),
    path('my/offers/', MyOffers.as_view(), name='list'),

]
