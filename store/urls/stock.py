from django.urls import path

# My imports -----------------------------------------------------------------
from ..views import AddStock
from ..views import StockDetails
from ..views import UpdateStock, RemoveStock

from search.views import ItemSearch
from interest.views import AddOrder

app_name = 'stock'
urlpatterns = [
    path('search/', ItemSearch.as_view(), name='search'),

    path('add/', AddStock.as_view(), name='add'),
    path('<int:pk>/', StockDetails.as_view(), name='details'),
    path('<int:pk>/edit/', UpdateStock.as_view(), name='update'),
    path('<int:pk>/remove/', RemoveStock.as_view(), name='remove'),
    path('<int:pk>/order/', AddOrder.as_view(), name='order'),

]
