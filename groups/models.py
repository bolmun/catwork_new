from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(AbstractUser):

    bio = models.TextField()
    members = models.ManyToManyField("users.User", blank=True, related_name="group")
    city = models.CharField(max_length=80, blank=True, null=True)
    group_avatar = models.ImageField(upload_to="group_avatars", null=True, blank=True)

    def count_members(self):
        return self.members.count()
