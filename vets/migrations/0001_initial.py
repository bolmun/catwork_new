# Generated by Django 2.2.5 on 2021-02-11 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('visit_date', models.DateField()),
                ('vet_title', models.CharField(max_length=100)),
                ('symptom', models.CharField(default='', max_length=200)),
                ('diagnosis', models.CharField(default='', max_length=200)),
                ('expense', models.IntegerField(blank=True, null=True)),
                ('receipt', models.FileField(blank=True, null=True, upload_to='')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vets', to='cats.Cat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('visit_date', models.DateField()),
                ('vet_title', models.CharField(max_length=100)),
                ('vaccination', models.CharField(blank=True, max_length=100, null=True)),
                ('expense', models.IntegerField(blank=True, null=True)),
                ('receipt', models.FileField(blank=True, null=True, upload_to='')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vcs', to='cats.Cat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
