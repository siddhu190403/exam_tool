from django.db import models

# Create your models here.
class Testing:
    price : int
    desc : str

    def getPrice():
        return price

class sample(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
