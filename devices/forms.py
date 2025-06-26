from django import forms

from .models import NetworkDevice


class NetworkDeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkDevice
        fields = [
            "name",
            "ip_address",
            "device_type",
            "vendor",
            "platform",
            "username",
            "password",
            "port",
            "description",
            "location",
            "is_active",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "ip_address": forms.TextInput(attrs={"class": "form-control"}),
            "device_type": forms.Select(attrs={"class": "form-control"}),
            "vendor": forms.Select(attrs={"class": "form-control"}),
            "platform": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "port": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
