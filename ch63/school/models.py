from django.db import models
from school.managers import CustomStudentManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.CharField(max_length=30,unique=True,null=True)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()
    admission_date = models.DateTimeField()

    # objects = models.Manager() # default manager
    students = models.Manager() # custom manager we can create multiple managers meaning we can have multiple ways to access the model data .e.g. Student.students.all() or Student.objects.all()
    custom = CustomStudentManager() # using custom manager

    def __str__(self):
        return self.name
    

