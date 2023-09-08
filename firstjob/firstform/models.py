from django.db import models

class FirstFormModel(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  # renames the instances of the model
  # with their firstname
  def __str__(self):
        return self.firstname

class SecondFormModel(models.Model):
  address = models.CharField(max_length=255)
  hobby = models.CharField(max_length=255)

  # renames the instances of the model
  # with their firstname
  def __str__(self):
        return self.address