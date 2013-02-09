from django.conf.urls import patterns, url
from django.views.generic import TemplateView
# from django.core.urlresolvers import reverse

from petition.views import PetitionView

urlpatterns = patterns('',
    url(r'^succes/$', TemplateView.as_view(
        template_name='petition/success.html'), name='petition_success'),
    # For some reason reverse() causes an ImproperlyConfigured error.
    url(r'^$', PetitionView.as_view(), name='petition_form')
)
