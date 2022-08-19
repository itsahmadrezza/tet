from django.db import models

# Create your models here.

class Counseling(models.Model):
    name = models.CharField(max_length=64)
    number = models.IntegerField()

    def __str__(self):
        return f"the '{self.name}', number is '{self.number}'"