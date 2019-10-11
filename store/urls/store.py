from django.urls import path

# My imports -----------------------------------------------------------------
from ..views import SetupStore, store_home
from ..views import StoreDetails
from ..views import UpdateStore, DeleteStore

from search.views import ItemSearch
from interest.views import AddOffer

app_name = 'store'
urlpatterns = [
    path('', store_home, name='home'),
    path('search/', ItemSearch.as_view(), name='search'),

    path('setup/', SetupStore.as_view(), name='setup'),
    path('<int:pk>/', StoreDetails.as_view(), name='details'),
    path('<int:pk>/edit/', UpdateStore.as_view(), name='update'),
    path('<int:pk>/remove/', DeleteStore.as_view(), name='delete'),

]
