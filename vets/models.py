from django.db import models
from core import models as core_models


class Vet(core_models.TimeStampedModel):

    visit_date = models.DateField()
    vet_title = models.CharField(max_length=100)
    cat = models.ForeignKey("cats.Cat", related_name="vets", on_delete=models.CASCADE)
    symptom = models.CharField(max_length=200, default="")
    diagnosis = models.CharField(max_length=200, default="")
    expense = models.IntegerField(blank=True, null=True)
    receipt = models.FileField(blank=True, null=True)


class Vaccination(core_models.TimeStampedModel):
    visit_date = models.DateField()
    vet_title = models.CharField(max_length=100)
    cat = models.ForeignKey("cats.Cat", related_name="vcs", on_delete=models.CASCADE)
    vaccination = models.CharField(max_length=100, blank=True, null=True)
    expense = models.IntegerField(blank=True, null=True)
    receipt = models.FileField(blank=True, null=True)