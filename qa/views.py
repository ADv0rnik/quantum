from django.contrib import messages

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
        detectors = Detector.objects.all()
        if request.method == "POST":
            if detector_code := request.POST.get('detector'):
                det = Detector.objects.prefetch_related("session_detector").filter(code=detector_code).first()
                session_data = det.session_detector.all()
                sessions = []
                for session in session_data:
                    rois = []
                    for spectrum in session.spectrum.all():
                        fwhm = spectrum.fwhm
                        nucl_name = spectrum.nuclide.name
                        pulsmax = spectrum.pulsmax
                        centroid = spectrum.centroid
                        netcounts = round(spectrum.counts_per_second, 2)
                        decay_corr = round(spectrum.calculate_decay_correction, 2)
                        rois.append({
                            "name": nucl_name,
                            "fwhm": fwhm,
                            "pulsmax": pulsmax,
                            "centroid": centroid,
                            "netcounts": netcounts,
                            "decay_corr": decay_corr
                        })
                    sessions.append({
                        "det": det,
                        "session": session,
                        "rois": rois
                    })
                context = {
                    "sessions": sessions,
                    "detector": det,
                    "detectors": detectors,
                }
            else:
                context = {"detectors": detectors}
                messages.info(request, "Please select a detector")
    except Exception:
        return render(request, 'server_error.html', context={})
    else:
        print(context)
        return render(
            request,
            'dashboard.html',
            context=context
        )
