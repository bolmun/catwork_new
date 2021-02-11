from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from . import models


@admin.register(models.Group)
class CustomGroupAdmin(GroupAdmin):

    list_display = ("name", "city", "group_avatar", "count_members")
