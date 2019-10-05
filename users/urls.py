from django.urls import path

from review.views import create_review

from .views import UpdateProfile, DeleteView
from .views import ProfileDetails


app_name = 'user'
urlpatterns = [
    path('<int:pk>/', ProfileDetails.as_view(), name='details'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', UpdateProfile.as_view(), name='update'),
    path('<int:pk>/review/', create_review, name='review_create'),

]
