from django.db import models


# Create your models here.
class Budget(models.Model):
    amount = models.DecimalField(default=0)
