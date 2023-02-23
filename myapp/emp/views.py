from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp, TimeSheet
from django.contrib import messages


def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/home.html", {'emps': emps})


def add_emp(request):
    if request.method == "POST":

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")

        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        e = Emp()

        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone

        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
        # return redirect("/emp/home/")
    return render(request, "emp/add_emp.html", {})


def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    # return redirect("/emp/home/")
    # return render(request,"emp/add_emp.html",{})
    return render(request, "emp/home.html", {})


def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request, "emp/update_emp.html", {
        'emp': emp
    })


def do_update_emp(request, emp_id):
    if request.method == "POST":

        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")

        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Emp.objects.get(pk=emp_id)

        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone

        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
    # return redirect("/emp/home/")
    return render(request, "emp/home.html", {})


def add_timesheet(request):
    if request.method == "POST":
        reporting_manager = request.POST.get('reporting_manager')
        employees = request.POST.get('employees')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        add_timesheet = TimeSheet(reporting_manager=reporting_manager, employees=employees, date=date, start_time=start_time, end_time=end_time)
        messages.success(request,"Submitted")
    return render(request,'emp/timesheet.html')