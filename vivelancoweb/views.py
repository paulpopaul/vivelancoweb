from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import redirect, render

def home(request):
    return render(request,'skeleton.html')