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
    det = Detector.objects.filter(pk=1).first()
    if request.method == "POST":
        detector_code = request.POST.get('detector')
        det = Detector.objects.prefetch_related("session_detector").filter(code=detector_code).first()
        session_data = det.session_detector.all()
    else:
        session_data = Detector.objects.prefetch_related("session_detector").filter(code=det).first()

    return render(
        request,
        'dashboard.html',
        context={
            "sessions": session_data,
            "detector": det
        }
    )

# TODO: Add try catch
