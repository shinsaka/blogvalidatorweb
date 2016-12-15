from django.db import models
from django.db.models import Count, Case, When, Value, IntegerField


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


def get_images_by_sitename(sitename, sort='v'):

    if sort == 'v':
        order = '-eval_violence'
    elif sort == 'a':
        order = '-eval_adult'
    elif sort == 's':
        order = '-eval_spoof'
    else:
        order = '-eval_medical'

    return Item.objects.filter(site_name=sitename).annotate(
            eval_violence=Case(When(violence='VERY_UNLIKELY', then=Value(1)),
                               When(violence='UNLIKELY', then=Value(2)),
                               When(violence='POSSIBLE', then=Value(3)),
                               When(violence='LIKELY', then=Value(4)),
                               When(violence='VERY_LIKELY', then=Value(5)),
                               default=Value(0), output_field=IntegerField()),
            eval_adult=Case(When(adult='VERY_UNLIKELY', then=Value(1)),
                            When(adult='UNLIKELY', then=Value(2)),
                            When(adult='POSSIBLE', then=Value(3)),
                            When(adult='LIKELY', then=Value(4)),
                            When(adult='VERY_LIKELY', then=Value(5)),
                            default=Value(0), output_field=IntegerField()),
            eval_spoof=Case(When(spoof='VERY_UNLIKELY', then=Value(1)),
                            When(spoof='UNLIKELY', then=Value(2)),
                            When(spoof='POSSIBLE', then=Value(3)),
                            When(spoof='LIKELY', then=Value(4)),
                            When(spoof='VERY_LIKELY', then=Value(5)),
                            default=Value(0), output_field=IntegerField()),
            eval_medical=Case(When(medical='VERY_UNLIKELY', then=Value(1)),
                              When(medical='UNLIKELY', then=Value(2)),
                              When(medical='POSSIBLE', then=Value(3)),
                              When(medical='LIKELY', then=Value(4)),
                              When(medical='VERY_LIKELY', then=Value(5)),
                              default=Value(0), output_field=IntegerField()),
            ).values('name', 'url', 'violence', 'adult', 'spoof', 'medical',
                     'page_title', 'page_url', 'site_name', 'created_at', 'updated_at',
                     'eval_violence', 'eval_adult', 'eval_spoof', 'eval_medical'
            ).order_by(order)
