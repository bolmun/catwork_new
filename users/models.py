from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """custom user model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"
    LOGIN_NAVER = "naver"
    LOGIN_GOOGLE = "google"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "email"),
        (LOGIN_KAKAO, "Kakao"),
        (LOGIN_NAVER, "Naver"),
        (LOGIN_GOOGLE, "Google"),
    )

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    id_card = models.ImageField(upload_to="id_card", blank=True, null=True)
    id_card_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    bio = models.TextField(default="Please introduce yourself briefly")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
