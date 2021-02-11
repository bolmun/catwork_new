from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageModelAdmin:

    list_display = ("__str__", "created")


@admin.register(models.Conversation)
class ConversationModelAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "count_msgs",
        "count_participants",
    )
