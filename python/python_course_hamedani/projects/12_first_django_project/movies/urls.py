from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.index, name='movies_index'),
    # This view naming can be simplidied by adding app_name variable.
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
