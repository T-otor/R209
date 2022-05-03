from operator import index
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('formulaire.html', views.formulaire, name='formulaire'),
    path('traitement', views.traitement),
    path('show', views.show),
    path('show/ram', views.showram),
    path('show/ram/delete/<int:id>/', views.deleteram),
    path('show/ram/update/<int:id>', views.update),
    path('show/ram/updatetraitement/<int:id>', views.updatetraitement)
]