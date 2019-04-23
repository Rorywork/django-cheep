from django.db import models

# Create your models here.

class Cheepees(models.Model):
    name = models.CharField(max_length=60, blank=False)
    strap = models.CharField(max_length=100)
    backgroundImageUrl = models.TextField()
    cheepeeImageURL = models.TextField()
    cheepeeProductName = models.CharField(max_length=60, blank=False)
    cheepeeInfo = models.TextField()
     
    def __str__(self):	    
        
        return self.name
