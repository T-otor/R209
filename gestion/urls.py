from operator import index
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('ajout/ram/<int:id>', views.ajoutram),
    path('ajout/cpu/<int:id>', views.ajoutcpu),
    path('ajout/hdd/<int:id>', views.ajouthdd),
    path('formulaire.html', views.formulaire, name='formulaire'),
    path('traitement', views.traitement),
    path('traitementmarque', views.traitementmarque),
    path('show', views.show),
    path('show/ram', views.showram),
    path('show/ram/delete/<int:id>/', views.deleteram),
    path('show/ram/update/<int:id>', views.updateram),
    path('show/ram/updatetraitement/<int:id>', views.updateramtraitement),
    path('traitementcpu', views.traitementcpu),
    path('show/cpu', views.showcpu),
    path('show/cpu/update/<int:id>', views.updatecpu),
    path('show/cpu/delete/<int:id>', views.deletecpu),
    path('show/hdd/update/<int:id>', views.updatehdd),
    path('show/hdd/delete/<int:id>', views.deletehdd),
    path('show/hdd', views.showhdd),
    path('traitementhdd', views.traitementhdd),
    path('', views.index),
    path('ajout/marque/', views.ajoutemarque),
]