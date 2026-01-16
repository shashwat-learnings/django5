from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # CASCADE will delete profile if user is deleted and vice versa is not true
    # user = models.OneToOneField(User, on_delete=models.PROTECT) # PROTECT will prevent deletion of user if profile exists
    # user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}) # Limit choices to create profile for only staff users only, 
    # user = models.OneToOneField(User, on_delete=models.DO_NOTHING) # DO_NOTHING will do nothing on deletion of user 
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    

class Page(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=255)


    def __str__(self):
        return self.page_name
    
class Like(Page):
    page = models.OneToOneField(Page, on_delete=models.CASCADE,parent_link=True) # to change the behaviour when it simply inherit
    liked_by = models.IntegerField()

    def __str__(self):
        return f"{self.liked_by} likes "