from django.db import models

# Create your models here.
class Calculation(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    ADDITION = 'add'
    SUBTRACTION = 'sub'
    MULTIPLICATION = 'mul'
    OPERATION_CHOICES = [
        (ADDITION, 'Sumar'),
        (SUBTRACTION, 'Restar'),
        (MULTIPLICATION, 'Multiplicar'),
    ]
    operation = models.CharField(
        max_length=3,
        choices=OPERATION_CHOICES,
        default=ADDITION,
    )