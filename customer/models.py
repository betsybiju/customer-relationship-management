from django.db import models

class feedback(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=40)
	phone=models.IntegerField()
	msg=models.CharField(max_length=100)
# Create your models here.
class customer(models.Model):
	name=models.CharField(max_length=20)
	address=models.CharField(max_length=40)
	email=models.EmailField(max_length=40)
	phone=models.IntegerField()
	
