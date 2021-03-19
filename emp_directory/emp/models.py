from uuid import uuid4

from django.db import models


# Create your models here.

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, blank=True)
    age = models.IntegerField()
    address = models.TextField(max_length=1024)
    city = models.ForeignKey("City", on_delete=models.CASCADE, blank=True,
                             null=True)
    state = models.ForeignKey("State", on_delete=models.CASCADE, blank=True,
                              null=True)
    country = models.ForeignKey("Country", on_delete=models.CASCADE,
                                blank=True,null=True)
    bank_details = models.OneToOneField("BankDetail", on_delete=models.CASCADE, null=True, blank=True)
    skill_sets = models.ManyToManyField('SkillSet', blank=True)

    def __str__(self):
        return F"{self.first_name} {self.last_name}"


class City(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class State(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class BankDetail(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4)
    bank_id = models.CharField(max_length=12)
    bank_name = models.CharField(max_length=64)
    bank_ifsc = models.CharField(max_length=64)

    def __str__(self):
        return self.bank_id


class SkillSet(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Accounts(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4)
    emp = models.OneToOneField('Employee', on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return self.emp.first_name
