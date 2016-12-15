from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
import datetime
from .models import get_sitenames
from .models import get_images_by_sitename


def index(request):
    return render(request, 'index.html', {'sites': get_sitenames()})


def list(request, sitename, page='1', sort='v'):
    paginator = Paginator(get_images_by_sitename(sitename, sort), 100)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'sitename': sitename, 'items': items})
