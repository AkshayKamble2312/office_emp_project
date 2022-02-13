from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render,HttpResponse
from.models import Department,Role,Employee
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    if request.user.is_authenticated:
        templates = 'index.html'
        return render(request,templates)

    else:
        return redirect('/login')

    

@login_required
def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

@login_required
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        add_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        add_emp.save()
        return redirect('/all_emp')
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception Occured!! Employee Has Not Been Added")

@login_required
def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect('/all_emp')
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps':emps

    }
    return render(request,'remove_emp.html',context)


@login_required
def update_emp(request,emp_id =0):
    
    item=Employee.objects.filter(id=emp_id)
    print(item)
    for emp_id in item:
        if request.method=='POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = int(request.POST['salary'])
            bonus = int(request.POST['bonus'])
            phone = int(request.POST['phone'])
            dept = int(request.POST['dept'])
            role = int(request.POST['role'])
            update_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
            update_emp.save()
            return redirect('/view_all_emp.html')
        elif request.method=='GET':
            return render(request,'update_emp.html')
        else:
            return HttpResponse("An Exception Occured!! Employee Has Not Updated")


 
@login_required
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        
        if dept:
            emps = emps.filter(dept__name__icontains = dept)

        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps':emps
        }
        return render(request,'view_all_emp.html',context)

    elif request.method == 'GET':
        return render(request,'filter_emp.html')

    else:
        return HttpResponse('An Exception Occured')




def loginuser(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html')
            
        
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
   