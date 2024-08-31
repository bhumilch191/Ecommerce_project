from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class Login_user(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)  

    def __str__(self):
        return self.email  