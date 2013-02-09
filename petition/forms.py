from django.forms import ModelForm
from petition.models import Petition


class PetitionForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Petition
