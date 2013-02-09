from django import forms
from petition.models import Petition


class PetitionForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Petition

    def clean(self):
        if not (self.cleaned_data['voornaam'] and self.cleaned_data['familienaam']) and not (self.cleaned_data['organisatie']):
            raise forms.ValidationError('U moet voornaam en familienaam invullen, of organisatienaam.')
        return self.cleaned_data
