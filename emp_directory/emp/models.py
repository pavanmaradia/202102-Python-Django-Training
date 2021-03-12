from django.db import models


# Create your models here.

class Employee(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, blank=True)
    age = models.IntegerField()
    address = models.TextField(max_length=1024)

    def __str__(self):
        return F"{self.first_name} {self.last_name}"


