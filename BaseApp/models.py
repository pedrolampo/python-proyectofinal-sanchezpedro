from django.db import models

# Create your models here.
class Guitar(models.Model):
  name = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.CharField(max_length=150)

  def __str__(self):
    return f'{self.name}'

class Bass(models.Model):
  name = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.CharField(max_length=150)

  def __str__(self):
    return f'{self.name}'

class Client(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  email = models.EmailField()

  def __str__(self):
    return f'{self.name} {self.surname}'
