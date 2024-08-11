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
    try:
        if request.method == "POST":
            detector_code = request.POST.get('detector')
            det = Detector.objects.prefetch_related("session_detector").filter(code=detector_code).first()
            session_data = det.session_detector.all()
            sessions = []
            for session in session_data:
                rois = []
                for spectrum in session.spectrum.all():
                    fwhm = spectrum.fwhm
                    pulsmax = spectrum.pulsmax
                    centroid = spectrum.centroid
                    netcounts = round(spectrum.counts_per_second, 2)
                    decay_corr = round(spectrum.calculate_decay_correction, 2)
                    rois.append({
                        "fwhm": fwhm,
                        "pulsmax": pulsmax,
                        "centroid": centroid,
                        "netcounts": netcounts,
                        "decay_corr": decay_corr
                    })
                sessions.append({
                    "session": session,
                    "rois": rois
                })
    except Exception as e:
        return render(request, 'server_error.html', context={})
    else:
        context = {
                "sessions": sessions,
                "detector": det,
            }
        print(context)
        return render(
            request,
            'dashboard.html',
            context=context
        )
