from django.contrib import admin
from qa.models import Detector, SessionData, Roi, Nuclide


class SpectrumInline(admin.TabularInline):
    model = Roi
    readonly_fields = ("created_at",)
    fields = ["centroid", "net_count", "nuclide"]


@admin.register(Detector)
class DetectorAdmin(admin.ModelAdmin):
    list_display = ("code", "fine_gain", "coarse_gain",)
    readonly_fields = ("created_at", "updated_at",)


@admin.register(SessionData)
class SessionDataAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    inlines = [SpectrumInline]


@admin.register(Roi)
class RoiAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", )
    fields = ["session_data", "centroid", "net_count", "roi_type", "nuclide"]


admin.site.register(Nuclide)
