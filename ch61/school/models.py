from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.CharField(max_length=30,unique=True,null=True)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()
    admission_date = models.DateTimeField()

    def __str__(self):
        return self.name
    

