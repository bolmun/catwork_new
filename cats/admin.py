from django.contrib import admin
from . import models


@admin.register(
    models.CoatColor, models.CoatPattern, models.Marking, models.Characteristic
)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("title", "used_by")

    def used_by(self, obj):
        return obj.cats.count()


@admin.register(models.Cat)
class CatAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "city",
                    "birthdate",
                    "estimated_age",
                    "gender",
                    "is_neutered",
                )
            },
        ),
        (
            "Appearance & Character",
            {
                "fields": (
                    "coat_color",
                    "coat_length",
                    "coat_pattern",
                    "marking",
                    "characteristic",
                )
            },
        ),
        (
            "Family Info",
            {"fields": ("mom_cat", "dad_cat", "bro_sis")},
        ),
        (
            "More Detail",
            {"fields": ("rescue_story", "care_taker")},
        ),
        (
            "SNS",
            {"fields": ("instagram_id", "facebook_id", "tiktok_id", "youtube_url")},
        ),
    )

    list_display = (
        "name",
        "city",
        "gender",
        "is_neutered",
        "birthdate",
        "count_age",
        "estimated_age",
        "care_taker",
    )

    raw_id_fields = ("care_taker",)

    list_filter = ("coat_color", "coat_length", "coat_pattern")

    filter_horizontal = ("bro_sis", "marking", "characteristic")

    search_fields = ("=city", "^care_taker__username", "=name")
