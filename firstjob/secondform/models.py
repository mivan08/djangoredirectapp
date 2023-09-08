from django.db import models

class Detail(models.Model):
  hobby = models.CharField(max_length=255)
  address = models.CharField(max_length=255)