from django.db import models

class Transcation(models.Model):
    TRANSCATION_TYPES = [('Income','Income'),
                        ('Expense','Expense')]
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=30,decimal_places=2)
    Transcation_type = models.CharField(max_length=20,choices= TRANSCATION_TYPES)
    date = models.DateField()
    category = models.CharField(max_length=255)