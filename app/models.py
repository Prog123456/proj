from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver








class Employees(models.Model):
    GENDER = {
        "F": "Female",
        "M": "Male",
        
    }
    STATUS = {
        "Married": "Married",
        "Unmarried": "Unmarried",
        "Widow":"Widowed",
        "Divorced":"Divorced",
        
    }
    DEPARTMENT = {
        "CRM": "Customer Relationship Management",
        "E&P": "Editorial and  Publications",
        "R&D":"Research and Development",
        "S&D":"Software and Development",
        
    }
    DESIGNATION = {
        "Jr.Software Developer": "Junior Software Developer",
        "Jr.Technical Writer": "Junior Technical Writer",
        "BDE":"Business Development Executive",
        "Reasearch Associate":"Research Associate",
        "Assistant Editor":"Assistant Editor",
        "Client Relationship Associate":"Client Relationship Associate",
        "Research Assistant":"Research Assistant",
        "Executive Assistant":"Executive Assistant",
        "Assistant Team Lead":"Assistant Team Lead",
        "Team Lead":"Team Lead",
        
    }
    id = models.AutoField(primary_key=True)
   
    profile_pic = models.ImageField(upload_to='profile_pics/')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    husband_name  = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    blood_group= models.CharField(max_length=10)
    
    employee_id=models.CharField(max_length=12)
    
    department= models.CharField(choices=DEPARTMENT,max_length=50)
    designation= models.CharField(choices=DESIGNATION,max_length=50)
    gender= models.CharField(choices=GENDER,max_length=50)
    
    marital_status=models.CharField(choices=STATUS,max_length=50)
    date_of_joining=models.DateField()
    door_no=models.CharField(max_length=10)

    address = models.TextField()
    country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True) 
    city = models.ForeignKey('cities_light.Region', on_delete=models.SET_NULL, null=True, blank=True)

   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


















