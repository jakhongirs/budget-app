from django.db import models


# Create your models here.
class Budget(models.Model):
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def call_date_time(self):
        return f"{self.datetime.date()}"
