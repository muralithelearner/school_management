from click import password_option
from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser



def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'loginpage.html')


def doLogin(request):
    if request.method =='POST':

        # Both are same process pattern was changed
        # email =request.POST.get('email')
        # password = request.POST.get('password')
        # user = EmailBackEnd.authenticate(request, username=email, password=password)

        # if user is None:
        #     user = authenticate(request, username=email, password=password)
        
        

        user =EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'))
        
        # Now we can log in both user name adn mail this is option not mandatary
        if user is None:
            user = authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user!= None:
            login(request,user)
            user_type = user.user_type
            if user_type=='1':
                return redirect('hod/home')
            elif user_type =='2':
                pass
            elif user_type =='3':
                pass
            else:
                messages.error(request,'Email or Password are Invalid')
                return redirect('login')
        else:
            messages.error(request,'Email or Password is Invalid')
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect(LOGIN)   

def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    return render(request,'profile.html',{'user':user})

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method =="POST":
        profile_pic =request.FILES.get('profile_pic')
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        # email =request.POST.get('email')
        # username =request.POST.get('username')
        password =request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name= last_name
            # customuser.profile_pic =profile_pic
            
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic

            if password !=None and password != "":
                customuser.set_password(password)    
            customuser.save()
            messages.success(request,'Your profile is  update succefully')                
            redirect('profile')            

        except:
             messages.error(request,'Your data update is faild')
    return render(request,'profile.html')
        


    




