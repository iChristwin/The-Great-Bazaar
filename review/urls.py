from django.urls import path

from .views import EditReview
from .views import ReviewDetails, DeleteReview


app_name = 'review'
urlpatterns = [
    path('review/<int:id>/', ReviewDetails.as_view(), name='review_details'),
    path('review/<int:id>/edit/', EditReview.as_view(), name='review_edit'),
    path('review/<int:id>/delete/', DeleteReview.as_view(), name='review_delete'),

]
