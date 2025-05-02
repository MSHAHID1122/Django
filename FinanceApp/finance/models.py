from django.db import models
from django.contrib.auth.models import User
class Transcation(models.Model):
    TRANSCATION_TYPES = [('Income','Income'),
                        ('Expense','Expense')]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=30,decimal_places=2)
    Transcation_type = models.CharField(max_length=20,choices= TRANSCATION_TYPES)
    date = models.DateField()
    category = models.CharField(max_length=255)
    def __str__(self):
        return str(self.title)