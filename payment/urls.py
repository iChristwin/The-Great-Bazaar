from django.urls import path

from .views import proceed_deposit, confirm_deposit
from .views import cashout_proceed, ConfirmDeposit


app_name = 'payment'
urlpatterns = [
    path('<int:pk>/confirm/', ConfirmDeposit.as_view(), name='confirm'),
#    path('<int:pk>/confirm/', confirm_deposit, name='confirm'),
    path('<int:pk>/<bank>/transfer/', proceed_deposit, name='proceed'),
    path('<int:pk>/cashout/', cashout_proceed, name='cashout'),

]
