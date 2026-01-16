from django.db import models

# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    join_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(BaseModel):
    roll = models.IntegerField(unique=True)
    fees = models.IntegerField()
    join_date = None

    def __str__(self):
        return f"{self.name} (Roll: {self.roll})"
    
class Teacher(BaseModel):
    salary = models.IntegerField()  

    def __str__(self):
        return f"{self.name} - {self.age} years"

class Contractor(BaseModel):
    payment = models.IntegerField() 
    join_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - Contract for {self.payment} months"
    

# Note: The BaseModel is abstract and won't create a separate table in the database.
# Models for Student, Teacher, and Contractor inherit common fields from BaseModel.

#Multi Table Inheritance Example
class ExamCenter(models.Model):
    center_name = models.CharField(max_length=100)
    center_city = models.CharField(max_length=200)


    def __str__(self):
        return self.center_name

class Candidate(ExamCenter):  # Inheriting from ExamCenter, it will create a separate table and one-to-one relationship with ExamCenter
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    def __str__(self):
        return f"{self.name} - Reg No: {self.roll}"
    


# Note: In Multi Table Inheritance, each model gets its own database table.
# The Candidate model will have a one-to-one relationship with the ExamCenter model.
# In this example, each candidate is associated with an exam center.
# so if we create a Candidate instance, it will also create an ExamCenter instance.
# if you delete the ExamCenter instance, the associated Candidate instance will also be deleted due to cascading delete behavior.
# Similarly, if you delete a Candidate instance, the associated ExamCenter instance will also be deleted because of the one-to-one relationship.

#proxy model example
# A proxy model allows you to change the behavior of an existing model without changing its fields or database schema.
# It uses the same database table as the original model but can have different methods or behaviors.
class Proudct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    
class DiscountedProduct(Proudct):  # Proxy model
    class Meta:
        proxy = True  # This indicates that it's a proxy model
        ordering = ['id']  # Change default ordering