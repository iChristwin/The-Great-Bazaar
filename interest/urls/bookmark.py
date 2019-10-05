from django.urls import path

# My imports -----------------------------------------------------------------
from ..views import add_bookmark, remove_bookmark, get_bookmarks


app_name = 'interest'
urlpatterns = [
    path('<int:pk>/add/', add_bookmark, name='add'),
    path('<int:pk>/remove/', remove_bookmark, name='remove'),
    path('my/bookmarks/', get_bookmarks, name='list'),

]
