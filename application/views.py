from django.shortcuts import render,get_object_or_404
from .models import Employee
from django.utils import timezone
from .forms import Employeeform
from django.shortcuts import redirect
# Create your views here.
def index(request):
    Employees = Employee.objects.all()
    return render(request,'application/index.html',{'Employee':Employees})


def base(request):
    
    return render(request,'application/home.html')

def Employee_detail(request, pk):
    employee= get_object_or_404(Employee, pk=pk)
    return render(request, 'application/Employee_detail.html',{'employee':employee})


def Employee_new(request):
    if request.method=='Post':
       form=Employeeform(request.POST)
       if form.is_valid():
           employee=form.save(commit=False)
           employee.E_id=request.user
           employee.E_sal_date=timezone.now()
           employee.save()
           return redirect('Employee_Detail',pk=emp.pk)
    else:
        form=Employeeform()
    return render(request,'application/Employee_new.html',{'form':form})   

def Employee_edit(request, pk):
    employee=get_object_or_404(Employee, pk=pk)
    if request.method=='Post':
        form=Employeeform(request.POST)
        if form.is_valid():
            employee=form.save(commit=False)
            employee.E_id=request.user
            employee.E_sal_date=timezone.now()
            employee.save()
            return redirect('Employee_Detail',pk=emp.pk)
    else:
        employee=Employeeform(instance=employee)

    return render(request,'application/Employee_edit.html',{'form':employee})    