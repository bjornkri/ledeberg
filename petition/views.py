from django.views.generic.edit import CreateView
from petition.models import Petition
from petition.forms import PetitionForm


class PetitionView(CreateView):
    form_class = PetitionForm
    model = Petition
    success_url = '/petition/succes/'
