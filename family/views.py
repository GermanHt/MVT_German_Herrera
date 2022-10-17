from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Family

# Create your views here.

def showmembers(request):
    members = Family.objects.all()
    return render(request,'template.html', {
        "members" : members
    })

