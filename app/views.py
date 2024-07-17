from django.shortcuts import render,redirect
from .models import Employees
from django.db import IntegrityError
from .forms import EmployeeForm

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import EmployeeForm
from .models import Employees
from cities_light.models import Country, Region,SubRegion

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Correct redirect to the home view
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})
def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country_id=country_id).order_by('name')
    return JsonResponse(list(regions.values('id', 'name')), safe=False)

def load_cities(request):
    region_id = request.GET.get('region_id')
    cities = SubRegion.objects.filter(region_id=region_id).order_by('name')
    return JsonResponse(list(cities.values('id', 'name')), safe=False)
# Create your views here.
def home(request):
    employee=Employees.objects.all()
    
    return render(request,'home.html',{'employee':employee})


