from django.contrib import admin
from .models import TransactionModel,Goal
# Register your models here.
admin.site.register(TransactionModel)
admin.site.register(Goal)
