from django.contrib import admin
from . import models


@admin.register(models.Doc)
class DocModelAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Cat",
            {"fields": ("cat",)},
        ),
        (
            "Applicant Basic Info",
            {
                "fields": (
                    "applicant",
                    "mobile",
                    "birthdate",
                    "address",
                )
            },
        ),
        (
            "SNS",
            {
                "fields": (
                    "instagram_id",
                    "facebook_id",
                )
            },
        ),
        (
            "Circumstance",
            {
                "fields": (
                    "housing_type",
                    "home_photo",
                    "protect_window",
                    "protect_door",
                )
            },
        ),
        (
            "Family Status",
            {
                "fields": (
                    "married",
                    "family_members",
                    "companion_animals",
                    "family_agreement",
                )
            },
        ),
        (
            "Finance",
            {
                "fields": (
                    "monthly_budget",
                    "urgent_budget",
                    "budget_how",
                )
            },
        ),
        (
            "Plan",
            {
                "fields": (
                    "first_ever_cat",
                    "daily_available_hours",
                    "weekend_available_hours",
                    "reason_adopt",
                )
            },
        ),
    )

    list_display = (
        "cat",
        "applicant",
        "birthdate",
        "mobile",
        "first_ever_cat",
        "id_card_verification",
    )
    raw_id_fields = ("cat", "applicant")
    ordering = (
        "cat",
        "applicant",
        "birthdate",
    )
    search_fields = ("=cat", "^applicant__username")
