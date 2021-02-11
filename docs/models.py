import datetime
from django.db import models
from core import models as core_models
from phonenumber_field.modelfields import PhoneNumberField


class AbstractItem(core_models.TimeStampedModel):

    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class HousingType(AbstractItem):
    class Meta:
        verbose_name_plural = "House Types"


class Doc(core_models.TimeStampedModel):

    cat = models.ForeignKey("cats.Cat", related_name="docs", on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        "users.User", related_name="docs", on_delete=models.CASCADE
    )
    mobile = PhoneNumberField()
    birthdate = models.DateField(null=False, default=datetime.date.today)
    address = models.CharField(max_length=200, default="", null=False)
    housing_type = models.ForeignKey(
        "HousingType", related_name="docs", on_delete=models.SET_NULL, null=True
    )
    home_photo = models.ImageField()
    instagram_id = models.CharField(max_length=20, null=True, blank=True)
    facebook_id = models.CharField(max_length=20, null=True, blank=True)
    daily_available_hours = models.IntegerField(
        default=10, help_text="How much time per day can you spend with the cat?"
    )
    weekend_available_hours = models.IntegerField(
        default=10, help_text="How much time per weekend can you spend with the cat?"
    )
    married = models.BooleanField(default=True)
    family_members = models.CharField(
        max_length=100,
        null=False,
        default="",
        help_text="Please describe the family members living with you. (Ex. Spouse, 2 teenagers)",
    )
    companion_aminals = models.CharField(
        max_length=100,
        null=False,
        default="",
        help_text="Please describe the companion animals living with you. (Ex. 1 Labrador Retriever, 2 Domestic Cats)",
    )
    family_agreement = models.BooleanField(default=False)
    monthly_budget = models.IntegerField(default=500000)
    urgent_budget = models.IntegerField(default=5000000)
    budget_how = models.TextField(
        default="", help_text="Please tell us how you plan to finance your budget."
    )
    protect_window = models.BooleanField(default=False)
    protect_door = models.BooleanField(default=False)
    first_ever_cat = models.BooleanField(default=False)
    reason_adopt = models.TextField(default="")

    def __str__(self):
        return f"{self.applicant} | {self.cat} Adoption application"

    def id_card_verification(self):
        if self.applicant.id_card_verified:
            return True
        else:
            return False