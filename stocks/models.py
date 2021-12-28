from django.db import models

# Create your models here.


class Stocks(models.Model):
	
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	ticker = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now=True)
