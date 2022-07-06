from django.http import HttpResponse
from django.shortcuts import render
from  .forms import addstudentform
# Create your views here.
from .models import Student
def register(request):
    form=addstudentform()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=addstudentform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'success.html')
        else:
            return HttpResponse("Please provide valid details")
    return render(request,'userregistration.html',context)

def studentlist(request):
    context={}
    ob1=Student.objects.all()
    context={'data':ob1}
    return render(request,'student_list.html',context)

def student_view(request,id):
    b1=Student.objects.get(student_code=id)
    context={}
    context["student"]=b1
    return render(request,"viewstudents.html",context)

def search(request):
    if request.method=='POST':
        phone_no=request.POST['phone']
        ob1=Student.objects.filter(phone=phone_no)
        context={'data':ob1}
        return render(request,'student_list.html',context)

def start(request):
    return render(request,'start.html')

def loadregister(request):
    form=addstudentform()
    context={}
    context["form"]=form
    return render(request,'userregistration.html',context)