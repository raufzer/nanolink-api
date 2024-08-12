from random import choices
from string import ascii_letters
from django.db import models
from django.conf import settings

# Create your models here.
class Link(models.Model):
    original_link = models.URLField()
    nano_link = models.URLField(blank=True, null=True)
    
    def shortner(self):
        while True:
            random_string = ''.join(choices(ascii_letters, k=6))
            new_link = settings.HOST_URL+'/'+random_string
            if not Link.objects.filter(nano_link=new_link).exists(): 
                ## checking the data base if already shorned link exist 
                # with the one generated if it is not exist it stop elese continue genreatinge
                break 
        return new_link
    def save(self, *args, **kwargs):
        if not self.nano_link:
            new_link = self.shortner()
            self.nano_link = new_link
        return super().save(*args, **kwargs)

       
    
    