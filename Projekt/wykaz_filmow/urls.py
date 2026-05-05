from django.urls import path

from . import views

app_name = 'wykaz_filmow'
urlpatterns = [
    path('', views.index, name='index'),
    path('filmy/', views.filmy, name ='filmy'),
    path('filmy/<int:film_id>/', views.film, name ='film'),
    path('nowy_film/', views.nowy_film, name='nowy_film'),
    path('nowa_ocena/<int:film_id>/', views.nowa_ocena, name='nowa_ocena'),
    path('edit_ocena/<int:ocena_id>/', views.edit_ocena, name='edit_ocena'),
    path('delete_ocena/<int:ocena_id>/', views.delete_ocena, name='delete_ocena'),
]