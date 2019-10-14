from django.urls import path

# My imports -----------------------------------------------------------------
from .views import AddItem, ItemInventory, item_home
from .views import ItemDetails, add_photo
from .views import EditItem, RemoveItem
from .views import ItemReserved, ListItems

from search.views import ItemSearch
from interest.views import AddOffer

app_name = 'item'
urlpatterns = [
    path('', item_home, name='home'),
    path('search/', ItemSearch.as_view(), name='search'),

    path('add/', AddItem.as_view(), name='add'),
    path('inventory/', ItemInventory.as_view(), name='inventory'),

    path('<int:pk>/', ItemDetails.as_view(), name='details'),
    path('<int:pk>/edit/', EditItem.as_view(), name='update'),
    path('<int:pk>/photo/', add_photo, name='photo'),
    path('<int:pk>/remove/', RemoveItem.as_view(), name='remove'),
    path('<int:pk>/reserved/', ItemReserved.as_view(), name='reserved'),
    path('<int:pk>/interested/', AddOffer.as_view(), name='interested'),

    path('all/', ListItems.as_view(), name='all'),
]
