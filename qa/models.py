from django.db import models
from django.utils.translation import gettext_lazy as _


class Detector(models.Model):
    code = models.CharField(
        _("Code"),
        max_length=100,
        unique=True
    )
    fine_gain = models.DecimalField(
        _("Fine Gain"),
        max_digits=10,
        decimal_places=2
    )
    coarse_gain = models.DecimalField(
        _("Coarse Gain"),
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.pk}"

    class Meta:
        verbose_name = _("Detector")
        verbose_name_plural = _("Detectors")
        ordering = ["pk"]


class Session(models.Model):
    detector = models.ForeignKey(
        Detector,
        on_delete=models.CASCADE,
        related_name="session_detector",
    )


class SessionData(models.Model):
    session = models.OneToOneField(
        Session,
        on_delete=models.CASCADE,
        related_name="data"
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.session.verbose_name} - {self.pk}"

    class Meta:
        verbose_name = _("Session Data")
        verbose_name_plural = _("Session Data")


class Spectrum(models.Model):
    class RoiType(models.TextChoices):
        ROI = "ROI", _("ROI type")
        INSERT = "INSERT", _("Insert")

    session_data = models.OneToOneField(
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.net_count}"

    class Meta:
        verbose_name = _("Spectrum")
        verbose_name_plural = _("Spectrums")
        ordering = ["created_at"]


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
