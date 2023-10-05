from django.db import models

# Create your models here.
#Thing classetitiy with attribues bame description quantity
class things(models):
    name = models.CharField(max_length=100)
    description=models.TextField()
    quantity=models.IntegerField()

