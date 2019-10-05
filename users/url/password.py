from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView


app_name = 'password'
urlpatterns = [
    path('change/', PasswordChangeView.as_view(),
         name='password_change'),
    path('change/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('reset/', PasswordResetView.as_view(),
         name='password_reset'),
    path('done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
