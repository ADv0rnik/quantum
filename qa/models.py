from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _


class Detector(models.Model):
    class DetectorType(models.TextChoices):
        hpge = "HPGE", _("HPGE")
        nai = "NAI", _("NaI(Tl)")

    code = models.CharField(
        _("Code"),
        max_length=100,
        unique=True
    )
    fine_gain = models.DecimalField(
        _("Fine Gain"),
        max_digits=10,
        decimal_places=4
    )
    coarse_gain = models.DecimalField(
        _("Coarse Gain"),
        max_digits=10,
        decimal_places=2
    )
    detector_type = models.CharField(
        choices=DetectorType.choices,
        default=DetectorType.hpge,
        max_length=100,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.pk}"

    class Meta:
        verbose_name = _("Detector")
        verbose_name_plural = _("Detectors")
        ordering = ["pk"]


class SessionData(models.Model):
    detector = models.OneToOneField(
        Detector,
        on_delete=models.CASCADE,
        related_name="session_detector",
    )
    sample_name = models.CharField(
        verbose_name=_("Sample Name"),
        max_length=255,
        blank=True,
        null=True
    )
    roi_file = models.CharField(
        verbose_name=_("ROI File"),
        max_length=255
    )
    qa_prep = models.CharField(
        verbose_name=_("QA Prep"),
        max_length=255
    )
    lifetime = models.DecimalField(
        verbose_name=_("Lifetime"),
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Description of the measurement session e.g. sample id in the logbook"),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def date_to_string(self):
        date = str(self.created_at)
        dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f%z")
        formatted_date = dt.strftime("%B %d %Y - %H:%M:%S")
        return formatted_date

    def __str__(self):
        return f"{self.sample_name}: {self.date_to_string()}"

    class Meta:
        verbose_name = _("Session Data")
        verbose_name_plural = _("Session Data")


class Nuclide(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        null=False,
    )
    energy = models.DecimalField(
        verbose_name=_("Energy"),
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.energy}"

    class Meta:
        verbose_name = _("Nuclide")
        verbose_name_plural = _("Nuclides")


class Roi(models.Model):
    class RoiType(models.TextChoices):
        ROI = "ROI", _("ROI")
        INSERT = "INSERT", _("Insert")

    session_data = models.ForeignKey(
        SessionData,
        on_delete=models.CASCADE,
        related_name="spectrum"
    )
    centroid = models.DecimalField(
        verbose_name=_("Centroid"),
        max_digits=10,
        decimal_places=2
    )
    net_count = models.PositiveBigIntegerField(
        verbose_name=_("Net Count")
    )
    roi_type = models.CharField(
        choices=RoiType.choices,
        default=RoiType.ROI,
        max_length=10
    )
    nuclide = models.ForeignKey(
        Nuclide,
        on_delete=models.CASCADE,
        related_name="roi"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Isotope: {self.nuclide.name}, with centroid in {self.centroid}"

    class Meta:
        verbose_name = _("ROI")
        verbose_name_plural = _("Spectra")
        ordering = ["created_at"]
