from django.contrib import admin
from . import models


@admin.register(models.Vet)
class VetAdmin(admin.ModelAdmin):

    list_display = (
        "visit_date",
        "vet_title",
        "cat",
        "diagnosis",
    )

    raw_id_fields = ("cat",)

    ordering = (
        "visit_date",
        "cat",
        "vet_title",
    )

    search_fields = ("=cat", "^vet_title")


@admin.register(models.Vaccination)
class VaccinationAdmin(admin.ModelAdmin):

    list_display = (
        "visit_date",
        "vet_title",
        "cat",
        "vaccination",
    )

    raw_id_fields = ("cat",)

    ordering = (
        "visit_date",
        "cat",
        "vet_title",
    )

    search_fields = ("=cat", "^vet_title")
