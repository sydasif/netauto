# Generated by Django 5.0.7 on 2024-07-03 13:00

from django.db import migrations


def create_missing_profiles(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Profile = apps.get_model("users", "Profile")

    for user in User.objects.all():
        if not hasattr(user, "profile"):
            Profile.objects.create(user=user)


def reverse_create_missing_profiles(apps, schema_editor):
    pass  # No need to reverse profile creation for missing profiles


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_profile_role"),
    ]

    operations = [
        migrations.RunPython(create_missing_profiles, reverse_create_missing_profiles),
    ]
