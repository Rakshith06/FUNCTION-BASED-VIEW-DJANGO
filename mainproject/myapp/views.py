from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from  myapp.models import Employee
from myapp.forms import EmployeeForm
# Create your views here.
def display(request):
    e=Employee.objects.all()

    d={'emp':e}
    return render(request,'myapp/index.html',d)
@login_required
def insert_view(request):
    f=EmployeeForm()
    if request.method=="POST":
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'form':f}
    return render(request,'myapp/insert.html',d)
@login_required
def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('/')
@login_required
def update_view(request,id):
    e=Employee.objects.get(id=id)
    if request.method=="POST":
        f=EmployeeForm(request.POST,instance=e)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'emp':e}
    return render(request,'myapp/update.html',d)
