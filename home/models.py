from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12, default="")
    wesite = models.CharField(max_length=122, default="")
    review = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

# demo models:


class Demo(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12, default="")
    address = models.CharField(max_length=122, default="")
    review = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
