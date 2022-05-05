from cProfile import label
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class FormRAM(ModelForm):
    class Meta:
        model = models.RAM
        fields = ('Marque', 'Modèle', 'Type', 'Capacité', 'SN')
        labels = {
        'Marque' : _('Marque'),
        'Modèle' : _('Modèle') ,
        'Type' : _('Type DDR (DDRX)'),
        'Capacité' : _('Capacité de la barette'),
        'SN' : ('Numéro de série')
        }


class FormCPU(ModelForm):
    class Meta:
        model = models.CPU
        fields = ('Marque', 'Modèle', 'Fréquence', 'SN')
        labels = {
            'Marque' : _('Marque'),
            'Modèle' : _('Modèle'),
            'Fréquence' : _('Fréquence'),
            'SN' : ('Numéro de série')
        }

class FormHDD(ModelForm):
    class Meta:
        model = models.HDD
        fields = ('Marque', 'Modèle', 'Type', 'Espace', 'SN')
        labels = {
            'Marque' : _('Marque'),
            'Modèle' : _('Modèle'),
            'Type' : _('Type'),
            'Espace' : _("Espace (préciser l'unité !)"),
            'SN' : ('Numéro de série')
        }

    
class FormMarque(ModelForm):
    class Meta:
        model = models.Marque
        fields = ('Marque',)
        labels = {
            'Marque' : _('Marque')
        }