from django.db import models

# class CustomStudentManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().order_by('name')

class CustomStudentManager(models.Manager):
    def get_stu_roll_range(self,roll_min, roll_max):
        return super().get_queryset().filter(roll__range=(roll_min, roll_max)).order_by('name')