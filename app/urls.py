
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('add_employee',views.create_employee,name="create_employee"),
    path('load_regions',views.load_regions,name="load_regions"),
    path('load_cities',views.load_cities,name="load_cities"),
]
