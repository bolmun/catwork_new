import math
from datetime import date
from django.db import models
from core import models as core_models

# Create your models here.
class AbstractItem(core_models.TimeStampedModel):

    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class CoatColor(AbstractItem):
    class Meta:
        verbose_name_plural = "Coat Colors"


class CoatPattern(AbstractItem):
    class Meta:
        verbose_name_plural = "Coat Patterns"


class Marking(AbstractItem):
    class Meta:
        verbose_name_plural = "Markings"


class Characteristic(AbstractItem):
    class Meta:
        verbose_name_plural = "Characteristics"


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="cat_photos")
    cat = models.ForeignKey("Cat", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Cat(core_models.TimeStampedModel):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    LENGTH_HAIRLESS = "hairless"
    LENGTH_SHORTHAIR = "shor hair"
    LEGNTH_MEDIUM_HAIR = "medium hair"
    LENGTH_LONGHAIR = "long hair"

    COAT_LENGTH = (
        (LENGTH_HAIRLESS, "Hairless"),
        (LENGTH_SHORTHAIR, "Shorthair"),
        (LEGNTH_MEDIUM_HAIR, "Medium hair"),
        (LENGTH_LONGHAIR, "Longhair"),
    )

    name = models.CharField(max_length=30)
    city = models.CharField(max_length=80)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    is_neutered = models.BooleanField(default=False)
    birthdate = models.DateField(null=True, blank=True)
    estimated_age = models.CharField(max_length=10, default=0, blank=True)
    coat_color = models.ForeignKey(
        CoatColor, related_name="cats", null=True, on_delete=models.SET_NULL
    )
    coat_length = models.CharField(choices=COAT_LENGTH, max_length=15)
    coat_pattern = models.ForeignKey(
        CoatPattern, related_name="cats", null=True, on_delete=models.SET_NULL
    )
    marking = models.ManyToManyField(Marking, blank=True)
    characteristic = models.ManyToManyField(Characteristic, blank=True)
    mom_cat = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="mom",
        on_delete=models.SET_NULL,
    )
    dad_cat = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="dad",
        on_delete=models.SET_NULL,
    )
    bro_sis = models.ManyToManyField("self", related_name="bs_cat", blank=True)
    rescue_story = models.TextField()
    care_taker = models.ForeignKey(
        "users.User",
        blank=False,
        null=False,
        related_name="cats",
        on_delete=models.PROTECT,
    )
    instagram_id = models.CharField(max_length=20, null=True, blank=True)
    facebook_id = models.CharField(max_length=20, null=True, blank=True)
    tiktok_id = models.CharField(max_length=20, null=True, blank=True)
    youtube_url = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def count_age(self):
        now = date.today()
        birth = self.birthdate
        if birth != None:
            difference = now - birth
            if difference.days > 365:
                year_age = math.floor((difference.days) / 365)
                age = f"{year_age} year(s) old"
            else:
                month_age = math.floor((difference.days) / 30)
                age = f"{month_age} months"
        else:
            age = self.estimated_age
        return age

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url

    def get_rest_photos(self):
        photos = self.photos.all()[1:5]
        return photos


class Photo(core_models.TimeStampedModel):
    caption = models.CharField(max_length=80, null=True, default="")
    file = models.ImageField(upload_to="cat_photos")
    cat = models.ForeignKey("Cat", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption