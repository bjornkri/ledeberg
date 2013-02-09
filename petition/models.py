from django.db import models


class Petition(models.Model):
    familienaam = models.CharField(max_length=255, blank=True, null=True)
    voornaam = models.CharField(max_length=255, blank=True, null=True)
    organisatie = models.CharField(max_length=255, blank=True, null=True)
    straat = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    gemeente = models.CharField(max_length=255)
    emailadres = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        name = ""
        if self.voornaam and self.familienaam:
            name = "%s %s" % (self.voornaam, self.familienaam)
        if self.organisatie:
            name += self.organisatie
        return "%s, %s, %s" % (name, self.straat,
            self.gemeente)
