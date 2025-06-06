from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Registration(AbstractUser):
  image = models.ImageField(upload_to='registration_image',blank=True,null=True)
  
  
  class Meta:
    db_table = 'registration'
    
    def __str__(self):
       return self.username