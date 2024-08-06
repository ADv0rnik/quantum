from django.shortcuts import render
from django.views.generic import ListView


def index(request):
    context = {
        "title": "Quantum - dashboard"
    }
    return render(request, 'dashboard.html', context=context)
