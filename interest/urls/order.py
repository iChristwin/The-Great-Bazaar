from django.urls import path

# My imports -----------------------------------------------------------------
from ..views import accept_order
from ..views import UpdateOrder, DeleteOrder
from ..views import MyOrders


app_name = 'offer'
urlpatterns = [
    path('<int:pk>/accept/', accept_order, name='accept'),
    # path('<int:pk>/cancel/', cancel_offer, name='cancel'),
    path('<int:pk>/update/', UpdateOrder.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteOrder.as_view(), name='delete'),
    path('my/offers/', MyOrders.as_view(), name='list'),

]
