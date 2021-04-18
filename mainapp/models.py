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
	key=models.CharField(max_length=50)
	value=models.TextField()
	id=models.IntegerField(primary_key=True)
	
	def __str__(self):
	    return(self.key[:30])

class Contact(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=80)
	desc=models.TextField()
	date=models.DateField()
	
	
	def __str__(self):
		return(self.name)
