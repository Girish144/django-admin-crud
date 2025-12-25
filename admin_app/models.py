from django.db import models

# Create your models here.
class product_model(models.Model):
    name=models.CharField(max_length=50)
    price=models.BigIntegerField()
    qty=models.IntegerField()
    loc=models.CharField(max_length=30)

    def __str__(self):
        return self.name