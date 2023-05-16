from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER=(
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )

    user_type = models.CharField(choices=USER, max_length=50,default=1)
    # user_type use in view.py for differnet logins
    profile_pic= models.ImageField(upload_to='media/profile_pic')

    # aditon option create in admin type is user type
    # now change the setting  for abstract

class Courses(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # change the time zone conf in setting file also
    # TIME_ZONE = 'Asia/Kolkata'  like this  

    def __str__(self):
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
       return self.session_start + ' To ' + self.session_end

class Student(models.Model):
    # admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    adress =models.TextField()
    gender =models.CharField(max_length=50)
    course_id =models.ForeignKey(Courses,on_delete=models.CASCADE)
    session_id= models.ForeignKey(Session_Year,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
       return self.admin.first_name + " " + self.admin.last_name
    
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    adress = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.admin.username
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course =models.ForeignKey(Courses,on_delete=models.CASCADE)
    staff =models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
