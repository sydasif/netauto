from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from users.views import role_required  # Import the role_required decorator

from .forms import NetworkDeviceForm
from .models import NetworkDevice


def device_list(request):
    """List all network devices with search functionality"""
    devices = NetworkDevice.objects.all()

    # Search functionality
    search_query = request.GET.get("search")
    if search_query:
        devices = devices.filter(
            Q(name__icontains=search_query)
            | Q(ip_address__icontains=search_query)
            | Q(vendor__icontains=search_query)
            | Q(location__icontains=search_query)
        )

    # Filter by device type
    device_type_filter = request.GET.get("device_type")
    if device_type_filter:
        devices = devices.filter(device_type=device_type_filter)

    # Filter by vendor
    vendor_filter = request.GET.get("vendor")
    if vendor_filter:
        devices = devices.filter(vendor=vendor_filter)

    context = {
        "devices": devices,
        "search_query": search_query,
        "device_type_filter": device_type_filter,
        "vendor_filter": vendor_filter,
        "device_types": NetworkDevice.DEVICE_TYPE_CHOICES,
        "vendors": NetworkDevice.VENDOR_CHOICES,
    }
    return render(request, "devices/device_list.html", context)


def device_detail(request, pk):
    """Show device details"""
    device = get_object_or_404(NetworkDevice, pk=pk)
    return render(request, "devices/device_detail.html", {"device": device})


@login_required
@role_required(["admin"])
def device_create(request):
    """Create a new device"""
    if request.method == "POST":
        form = NetworkDeviceForm(request.POST)
        if form.is_valid():
            device = form.save()
            messages.success(request, f'Device "{device.name}" created successfully!')
            return redirect("device_detail", pk=device.pk)
    else:
        form = NetworkDeviceForm()

    return render(
        request, "devices/device_form.html", {"form": form, "title": "Add New Device"}
    )


@login_required
@role_required(["admin"])
def device_update(request, pk):
    """Update an existing device"""
    device = get_object_or_404(NetworkDevice, pk=pk)

    if request.method == "POST":
        form = NetworkDeviceForm(request.POST, instance=device)
        if form.is_valid():
            device = form.save()
            messages.success(request, f'Device "{device.name}" updated successfully!')
            return redirect("device_detail", pk=device.pk)
    else:
        form = NetworkDeviceForm(instance=device)

    return render(
        request,
        "devices/device_form.html",
        {"form": form, "device": device, "title": f"Edit {device.name}"},
    )


@login_required
@role_required(["admin"])
def device_delete(request, pk):
    """Delete a device"""
    device = get_object_or_404(NetworkDevice, pk=pk)

    if request.method == "POST":
        device_name = device.name
        device.delete()
        messages.success(request, f'Device "{device_name}" deleted successfully!')
        return redirect("device_list")

    return render(request, "devices/device_confirm_delete.html", {"device": device})
