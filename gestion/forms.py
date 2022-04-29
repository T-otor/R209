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
