from django.urls import path

# My imports -----------------------------------------------------------------
from ..views import MakeBargain, UpdateBargain, DeleteBargain
from ..views import accept_bargain


app_name = 'bargain'
urlpatterns = [
    path('<int:pk>/add/', MakeBargain.as_view(), name='add'),
    path('<int:pk>/update/', UpdateBargain.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteBargain.as_view(), name='delete'),
    path('<int:pk>/accept/', accept_bargain, name='accept'),

]
