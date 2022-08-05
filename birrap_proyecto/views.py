from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime



def template_base(request):
    context = {

    }
    return render(request, "template_base.html", context=context)