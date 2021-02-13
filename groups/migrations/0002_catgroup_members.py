# Generated by Django 2.2.5 on 2021-02-11 18:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='catgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='group', to=settings.AUTH_USER_MODEL),
        ),
    ]
