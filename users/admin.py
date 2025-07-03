from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "location")
    list_filter = ("role", "location")
    search_fields = ("user__username", "location", "bio")


admin.site.register(Profile, ProfileAdmin)
