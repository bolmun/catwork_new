# Generated by Django 2.2.5 on 2021-02-11 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='care_taker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cat',
            name='characteristic',
            field=models.ManyToManyField(blank=True, to='cats.Characteristic'),
        ),
        migrations.AddField(
            model_name='cat',
            name='coat_color',
            field=models.ManyToManyField(blank=True, related_name='cats', to='cats.CoatColor'),
        ),
        migrations.AddField(
            model_name='cat',
            name='coat_pattern',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='cats.CoatPattern'),
        ),
        migrations.AddField(
            model_name='cat',
            name='dad_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dad', to='cats.Cat'),
        ),
        migrations.AddField(
            model_name='cat',
            name='marking',
            field=models.ManyToManyField(blank=True, related_name='cats', to='cats.Marking'),
        ),
        migrations.AddField(
            model_name='cat',
            name='mom_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mom', to='cats.Cat'),
        ),
    ]
