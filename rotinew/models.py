from django.db import models

class rotii(models.Model):
    user=models.CharField(max_length=64)
    value=models.IntegerField()

class login(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)

