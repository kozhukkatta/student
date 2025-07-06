from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from myapp.models import Course,Student,Details
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request,'home.html')

def course(request):
    return render(request,'course.html')

def student(request):
    stud=Course.objects.all()
    return render(request,'student.html',{'courses':stud})

def details(request):
    stud=Student.objects.all()
    return render(request,'details.html',{'studen':stud})

def cour_det(request):
    cou=Course.objects.all()
    return render(request,'cour_det.html',{'courses':cou})

def reg(request):
    stud=Course.objects.all()
    return render(request,'registration.html',{'courses':stud})

def add_course(request):
    if request.method == "POST":
        cname=request.POST['cname']
        fees=request.POST['fees']
        cou=Course(course_name=cname,fees=fees)
        cou.save()
        return redirect('cour_det')

def add_student(request):
    if request.method == "POST":
        sname=request.POST['sname']
        address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course=Course.objects.get(id=sel)
        stu=Student(sname=sname,address=address,age=age,jdate=jdate,course=course)
        stu.save()
        return redirect('details')
    return redirect('student')
    
def edits(request,pk):
    stud=Student.objects.get(id=pk)
    cou=Course.objects.all()
    cr=Student.objects.values('course').distinct()
    print(cr)
    return render(request,'edit_stud.html',{'std':stud,'courses':cou,'s':cr})

def up_student(request,pk):
    if request.method == "POST":
        stu=Student.objects.get(id=pk)
        stu.sname=request.POST['sname']
        stu.address=request.POST['address']
        stu.age=request.POST['age']
        stu.jdate=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        print(course1)
        stu.course=course1
        stu.save()
        return redirect('details')
    return redirect('student')

def deletes(request,pk):
    stud=Student.objects.get(id=pk)
    stud.delete()   
    return redirect('details')

def editc(request,pk):
    cor=Course.objects.get(id=pk)
    return render(request,'edit_cou.html',{'coru':cor})

def up_course(request,pk):
    if request.method == "POST":
        cour=Course.objects.get(id=pk)
        cour.course_name=request.POST['cname']
        cour.fees=request.POST['fees']
        cour.save()
        return redirect('cour_det')

def deletec(request,pk):
    cour=Course.objects.get(id=pk)
    cour.delete()
    return redirect('cour_det')

def add_stud(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        age=request.POST['age']
        mob=request.POST['mob']
        address=request.POST['address']
        username=request.POST['uname']
        email=request.POST['mail']
        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course=Course.objects.get(id=sel)
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('reg')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                det=Details(age=age,mob=mob,address=address,jdate=jdate,course=course,user=user)
                det.save()
        else:
            messages.info(request, "Password doesn't match")
            return redirect('reg')   
        return redirect('/')
    else:
        return render(request,'registration.html')