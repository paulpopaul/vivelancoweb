from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import redirect, render

from home.models import Home

def home(request):
    encabezado = Home.objects.all()
    context = {
        'encabezado': encabezado,
    }

    return render(request, 'skeleton.html')