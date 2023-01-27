from django.db import models

# Create your models here.

# CREATE TABLE profiledata(fname, lname, username, email)

class ProfileData(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()