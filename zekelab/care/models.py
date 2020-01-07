from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Caretaker(models.Model):
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    name = models.CharField(max_length=20)
    email = models.EmailField(default='')
    phone = models.IntegerField(default='0')
    dob = models.DateField(default='')
    milestone = models.IntegerField(default='0')
    review = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Careneeder(models.Model):
    cacreneeder_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    phone = models.IntegerField(default='')
    dob = models.DateField(default='0')
    payee = models.IntegerField(default='0')
    require = models.CharField(max_length=800, default='')

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
