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
    
