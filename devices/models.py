from django.db import models
from django.urls import reverse


class NetworkDevice(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Device hostname")
    ip_address = models.GenericIPAddressField(unique=True)

    DEVICE_TYPE_CHOICES = [
        ("router", "Router"),
        ("switch", "Switch"),
        ("firewall", "Firewall"),
        ("server", "Server"),
        ("other", "Other"),
    ]
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES)

    VENDOR_CHOICES = [
        ("cisco", "Cisco"),
        ("juniper", "Juniper"),
        ("arista", "Arista"),
        ("hp", "HP"),
        ("dell", "Dell"),
        ("other", "Other"),
    ]
    vendor = models.CharField(max_length=50, blank=True, choices=VENDOR_CHOICES)
    platform = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    port = models.IntegerField(default=22, help_text="SSH port")
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Network Device"
        verbose_name_plural = "Network Devices"

    def __str__(self):
        return f"{self.name} ({self.ip_address})"

    def get_absolute_url(self):
        return reverse("device_detail", kwargs={"pk": self.pk})
