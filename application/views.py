from django.shortcuts import render,get_object_or_404
from .models import Employee
from django.utils import timezone
# Create your views here.
def index(request):
    Employees = Employee.objects.all()
    return render(request,'application\index.html',{'Employee':Employees})


def base(request):
    
    return render(request,'application\home.html')

def Employee_detail(request, pk):
    employee= get_object_or_404(Employee, pk)
    return render(request, 'application\Employee_detail.html',{'employee':employee})

