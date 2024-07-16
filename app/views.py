from django.shortcuts import render,redirect
from .models import Employees
from django.db import IntegrityError
from .forms import EmployeeForm
# Create your views here.
def home(request):
    employee=Employees.objects.all()
    
    return render(request,'home.html',{'employee':employee})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                employee = form.save(commit=False)
                print(f"Saving employee: {employee}")
                employee.save()
                return redirect('home')
            except IntegrityError as e:
                print(f"IntegrityError: {e}")
                form.add_error(None, "There was an error saving the employee. Please ensure the country and city exist.")
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})
