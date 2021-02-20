from django.db import models

# Create your models here.
class Skill(models.Model):
    skill=models.CharField(max_length=50)
    level=models.IntegerField()

    def __str__(self):
	    	return(self.skill)
    
class idos(models.Model):
    what_you_do=models.CharField(max_length=70)

    def __str__(self):
	    	return(self.what_you_do)
    
class About(models.Model):
    about=models.TextField()

    def __str__(self):
	    	return(self.about[:30])

class Contact(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=80)
	desc=models.TextField()
	date=models.DateField()
	
	
	def __str__(self):
		return(self.name)
