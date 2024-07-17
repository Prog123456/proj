from django import forms
from cities_light.models import Country, Region, SubRegion
from .models import Employees

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = [
            'profile_pic', 'first_name', 'last_name', 'father_name', 'husband_name',
            'date_of_birth', 'blood_group', 'employee_id', 'department', 'designation',
            'gender', 'marital_status', 'date_of_joining', 'door_no', 'address', 'country', 'state', 'district'
        ]
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.all()
        self.fields['state'].queryset = Region.objects.none()
        self.fields['district'].queryset = SubRegion.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = Region.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Region queryset
        
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['district'].queryset = SubRegion.objects.filter(region_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        
        elif self.instance.pk:
            if self.instance.country:
                self.fields['state'].queryset = Region.objects.filter(country=self.instance.country).order_by('name')
            if self.instance.state:
                self.fields['district'].queryset = SubRegion.objects.filter(region=self.instance.state).order_by('name')
