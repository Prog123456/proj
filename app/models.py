from django.db import models
from cities_light.models import Country, Region,SubRegion

class Employees(models.Model):
    GENDER_CHOICES = [
        ("F", "Female"),
        ("M", "Male"),
    ]
    
    STATUS_CHOICES = [
        ("Married", "Married"),
        ("Unmarried", "Unmarried"),
        ("Widow", "Widowed"),
        ("Divorced", "Divorced"),
    ]
    
    DEPARTMENT_CHOICES = [
        ("CRM", "Customer Relationship Management"),
        ("E&P", "Editorial and Publications"),
        ("R&D", "Research and Development"),
        ("S&D", "Software and Development"),
    ]
    
    DESIGNATION_CHOICES = [
        ("Jr.Software Developer", "Junior Software Developer"),
        ("Jr.Technical Writer", "Junior Technical Writer"),
        ("BDE", "Business Development Executive"),
        ("Research Associate", "Research Associate"),
        ("Assistant Editor", "Assistant Editor"),
        ("Client Relationship Associate", "Client Relationship Associate"),
        ("Research Assistant", "Research Assistant"),
        ("Executive Assistant", "Executive Assistant"),
        ("Assistant Team Lead", "Assistant Team Lead"),
        ("Team Lead", "Team Lead"),
    ]

    id = models.AutoField(primary_key=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30, blank=True, null=True)
    husband_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10)
    employee_id = models.CharField(max_length=12)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=50)
    designation = models.CharField(choices=DESIGNATION_CHOICES, max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    marital_status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    date_of_joining = models.DateField()
    door_no = models.CharField(max_length=10)
    address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(SubRegion, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
