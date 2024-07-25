from django.contrib import admin
from qa.models import Detector, SessionData, Spectrum, Nuclide


class NuclideInline(admin.TabularInline):
    model = Nuclide.spectra.through


class SpectrumInline(admin.TabularInline):
    model = Spectrum
    readonly_fields = ("created_at",)
    fields = ["centroid", "net_count"]


@admin.register(Detector)
class DetectorAdmin(admin.ModelAdmin):
    list_display = ("code", "fine_gain", "coarse_gain",)
    readonly_fields = ("created_at", "updated_at",)


@admin.register(SessionData)
class SessionDataAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    inlines = [SpectrumInline]


@admin.register(Spectrum)
class SpectrumAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = ["get_nuclide"]
    inlines = [NuclideInline]
    exclude = ("spectrums",)

    def get_nuclide(self, obj):
        return [nuclide.name for nuclide in obj.nuclides.all()]


@admin.register(Nuclide)
class NuclideAdmin(admin.ModelAdmin):
    pass