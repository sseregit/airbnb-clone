from django.db import models
from . import managers

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    updated = models.DateTimeField(null=True,blank=True,auto_now=True)
    objects = managers.CustomModelManagers()

    class Meta:
        abstract = True
