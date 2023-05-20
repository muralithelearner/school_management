from django.shortcuts import render,redirect

def STAFF_HOME(request):
    return render(request,'staff/home.html')