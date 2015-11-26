from django.db import models

# Create your models here.
class Person(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	email = models.EmailField()
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
# class Message(models.Model):
# 	fromID = models.ForeignKey(Person)
# 	toID = models.ForeignKey(Person)
# 	msgBody = models.TextField()
# 	msgBody = models.TextField()