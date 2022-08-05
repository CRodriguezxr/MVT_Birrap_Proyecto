from django.http import HttpResponse
from django.shortcuts import render



def template_base(request):
    return render(request, "template_base.html", context={})