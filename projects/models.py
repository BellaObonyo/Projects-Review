from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(" User must have an email address")
        if not username:
            raise ValueError(" User must have an username!")    
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username=username,
        )
        user.email = email
        user.is_admin = True 
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user
        

class Users(AbstractBaseUser):
    username = models.CharField( max_length=50, unique=True)  
    email = models.CharField( max_length=50, unique=True) 
    profile = CloudinaryField('image', default='badgerz/image/upload/v1632511355/jellu_bmu8g6.jpg') 
    bio= models.TextField(null=True)
    last_login = models.DateTimeField(default=dt.datetime.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password_reset = models.CharField( max_length=50, default="e5viu3snjorndvd")    
    password = models.CharField( max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']        
    objects=MyAccountManager()
     
    def _str_(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    def save_project(self):
        self.save()
    
class myProjects(models.Model):
    title = models.CharField(max_length =100)
    image = CloudinaryField('image') 
    description = models.TextField()
    link = models.CharField(max_length =100)
    user=models.ForeignKey("Users",on_delete=models.CASCADE)

class Votes(models.Model):
    design=models.FloatField(default=0)
    usability=models.FloatField(default=0)
    content=models.FloatField(default=0)
    project=models.ForeignKey("myProjects",on_delete=models.CASCADE)
    user=models.ForeignKey("Users",on_delete=models.CASCADE)

