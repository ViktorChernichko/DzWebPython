from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name
