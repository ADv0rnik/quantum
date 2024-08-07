from django.shortcuts import render
from qa.models import Detector


def index(request):
    detectors = Detector.objects.all()
    context = {
        "title": "Quantum - dashboard",
        "detectors": detectors
    }
    return render(request, 'dashboard.html', context=context)


def get_data(request):
    pass
