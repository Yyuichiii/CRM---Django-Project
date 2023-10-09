from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from .forms import register_form,login_form,CreateRecordForm,UpdateRecordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'webapp/index.html')

# Register user
def register(request):
    if request.method=='POST':
        fm=register_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Your Account has been successfully created")
            return redirect('login')
    
    
    else:
        fm=register_form()
    
    return render(request,'webapp/register.html',{'form':fm})


# Login User

def login_(request):
    if request.method=='POST':
        
        fm=login_form(request,data=request.POST)
        if fm.is_valid():
            
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            

            user=authenticate(request,username=uname,password=upass)

            if user is not None:
                login(request,user)
                
                
                return redirect('dashboard')
    
    
    else:
        
        fm=login_form()
    
    return render(request,'webapp/login.html',{'form':fm})


# User logout
def user_logout(request):
    logout(request)
    messages.success(request, "You are logout successfully")
    return redirect('login')


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    my_record=Record.objects.all()
    context={
        'records':my_record
    }
    return render(request,'webapp/dashboard.html',context)

@login_required(login_url='login')
def create_record(request):
    fm=CreateRecordForm()

    if request.method=='POST':
        fm=CreateRecordForm(request.POST)

        if fm.is_valid():
            fm.save()
            messages.success(request, "The Record has been created successfully")

            return redirect('dashboard')
        
    return render(request,'webapp/create-record.html',{'form':fm})



@login_required(login_url='login')
def update_record(request,pk):
    record=Record.objects.get(id=pk)
    fm=UpdateRecordForm(instance=record)
    if request.method=='POST':
        fm=UpdateRecordForm(request.POST,instance=record)

        if fm.is_valid():
            fm.save()
            messages.success(request, "The Record has been updated successfully")

            return redirect('dashboard')
        
    return render(request,'webapp/update-record.html',{'form':fm})

@login_required(login_url='login')
def view_record(request,pk):
    record=Record.objects.get(id=pk)
    return render(request,'webapp/view-record.html',{'record':record})

@login_required(login_url='login')
def delete_record(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "The Record has been deleted successfully")
    return redirect('dashboard')