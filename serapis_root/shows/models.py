from django.db import models
from django.db.models import Case, When
from django import forms


class Show(models.Model):
    class Meta:
        ordering = ['-show_date']

    def __str__(self):
        return str(self.show_date)

    venue = models.CharField(max_length=100)

    show_date = models.DateTimeField()

    city = models.CharField(max_length=100)
