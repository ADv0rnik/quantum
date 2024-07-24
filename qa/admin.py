from django.contrib import admin
from qa.models import Detector, Session, SessionData, Spectrum, Nuclide


class NuclideInline(admin.TabularInline):
    model = Nuclide
    readonly_fields = ("created_at",)


class SpectrumInline(admin.TabularInline):
    model = Spectrum
    readonly_fields = ("created_at",)


class SessionDataInLine(admin.TabularInline):
    model = SessionData
    readonly_fields = ("created_at", "updated_at",)


@admin.register(Detector)
class DetectorAdmin(admin.ModelAdmin):
    list_display = ("code", "fine_gain", "coarse_gain",)
    readonly_fields = ("created_at", "updated_at",)


@admin.register(SessionData)
class SessionDataAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    inlines = [SpectrumInline]

# through - for m2m relationship
# @admin.register(Spectrum)
# class SpectrumAdmin(admin.ModelAdmin):
#     readonly_fields = ("created_at",)
#     inlines = [NuclideInline]
