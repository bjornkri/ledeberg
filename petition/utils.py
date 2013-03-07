from petition.models import Petition

def mailchimp_export():
    for p in Petition.objects.exclude(emailadres=""):
        print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (p.voornaam, p.familienaam,
            p.emailadres,
            " ".join(p.straat.split()[:-1]), p.straat.split()[-1], p.postcode,
            p.gemeente)