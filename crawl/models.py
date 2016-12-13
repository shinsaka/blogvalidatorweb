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


def get_sitenames():
    return Item.objects.values('site_name').annotate(icount=Count('site_name'))


def get_images_by_sitename(sitename):
    return Item.objects.filter(site_name=sitename)
