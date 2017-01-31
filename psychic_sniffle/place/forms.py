from django import forms
from redactor.widgets import RedactorEditor
from place.models import Place


class PlaceAdminForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ()
        widgets = {
           'description': RedactorEditor(),
        }
