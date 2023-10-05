from django.core.validators import MaxValueValidator,MinValueValidator,RegexValidator
from django.db import models

# Create your models here.
#Thing classetitiy with attribues bame description quantity
class Thing(models.Model):
    name = models.CharField(max_length=30,
                            unique=True,
                            blank=False,
                            validators=[RegexValidator(
                                message='name must be unique not blank and at most 30 char')])
    description=models.CharField(max_length=120,
                                 null=True,
                                 blank=True,
                                 validators=[RegexValidator(message='Description must be at most 120 characters')])
    quantity=models.IntegerField(validators=[MaxValueValidator(100),
                                             MinValueValidator(0)])

