from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField( max_length=255)
    city=models.CharField(max_length=70)
    roll=models.IntegerField()
    state = models.CharField(max_length=70)

    def __str__(self):
        return self.name  


