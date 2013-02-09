from django.db import models


class Petition(models.Model):
    naam = models.CharField(max_length=255)
    voornaam = models.CharField(max_length=255)
    straat = models.CharField(max_length=255)
    huisnummer = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    gemeente = models.CharField(max_length=255)
    emailadres = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s, %s, %s" % (self.voornaam, self.naam, self.straat,
            self.gemeente)
