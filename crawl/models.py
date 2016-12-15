from django.db import models
from django.db.models import Count


class Item(models.Model):
    name = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=1000, null=True)
    violence = models.CharField(max_length=200, null=True)
    adult = models.CharField(max_length=200, null=True)
    spoof = models.CharField(max_length=200, null=True)
    medical = models.CharField(max_length=200, null=True)
    page_title = models.CharField(max_length=1000, null=True)
    page_url = models.CharField(max_length=1000, null=True)
    site_name = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    values = {
        'VERY_UNLIKELY': 1,
        'UNLIKELY': 2,
        'POSSIBLE': 3,
        'LIKELY': 4,
        'VERY_LIKELY': 5,
    }

    def evalue_violence(self):
        return self.evalue(self.violence)

    def evalue_adult(self):
        return self.evalue(self.adult)

    def evalue_spoof(self):
        return self.evalue(self.spoof)

    def evalue_medical(self):
        return self.evalue(self.medical)

    def evalue(self, kind_column):
        """
        usage:
            x=models.Item.objects.all()[0]
            x.evalue(x.violence)
        """
        return self.values.get(kind_column) or 0


def get_sitenames():
    return Item.objects.values('site_name').annotate(icount=Count('site_name'))


def get_images_by_sitename(sitename):
    return Item.objects.filter(site_name=sitename)
