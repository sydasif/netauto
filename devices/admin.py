from django.contrib import admin

from .models import NetworkDevice


@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ip_address",
        "device_type",
        "vendor",
        "platform",
        "is_active",
        "created_at",
    ]
    list_filter = ["device_type", "vendor", "platform", "is_active"]
    search_fields = ["name", "ip_address", "description", "location"]
    readonly_fields = ["created_at", "updated_at"]
    list_per_page = 25

    fieldsets = (
        (
            "Basic Information",
            {"fields": ("name", "ip_address", "device_type", "vendor", "platform")},
        ),
        ("Connection Details", {"fields": ("username", "password", "port")}),
        (
            "Additional Information",
            {"fields": ("description", "location", "is_active")},
        ),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
