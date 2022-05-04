from operator import index
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('ajout/ram/<int:id>', views.ajoutram),
    path('ajout/cpu/<int:id>', views.ajoutcpu),
    path('formulaire.html', views.formulaire, name='formulaire'),
    path('traitement', views.traitement),
    path('show', views.show),
    path('show/ram', views.showram),
    path('show/ram/delete/<int:id>/', views.deleteram),
    path('show/ram/update/<int:id>', views.updateram),
    path('show/ram/updatetraitement/<int:id>', views.updateramtraitement),
    path('traitementcpu', views.traitementcpu),
    path('show/cpu', views.showcpu),
    path('show/cpu/update/<int:id>', views.updatecpu),
    path('show/cpu/delete/<int:id>', views.deletecpu),
]