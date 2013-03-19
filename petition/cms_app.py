from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PetitionHook(CMSApp):
    name = _("Petition")
    urls = ["petition.urls"]

apphook_pool.register(PetitionHook)
