from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Courses,Session_Year,CustomUser,Student,Staff
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request,'Hod/home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Courses.objects.all()
    session_year =Session_Year.objects.all()

    if request.method == 'POST':

        profile_pic = request.FILES.get('profile_pic')
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email = request.POST.get('email')
        username =request.POST.get('username')
        password =request.POST.get('password')
        adress = request.POST.get('adress')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,' email is already exist')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,' username is already exist')
            return redirect('add_student')  
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type= 3
            )
            user.set_password(password)
            user.save()

            course_id = Courses.objects.get(id= course_id)
            session_id = Session_Year.objects.get(id=session_id)

            student =Student(
                admin = user,
                adress =adress,
                session_id =session_id,
                gender =gender,
                course_id=course_id          
            )
            student.save()
            messages.success(request,user.first_name+" "+ user.last_name +"Are Succefully Added")
            return redirect('add_student')

    context ={
        'course' : course,
        'session_year' : session_year
    }
    return render(request,'Hod/add_student.html',context)

def VIEW_STUDENT(request):
    student =Student.objects.all()

    context ={
        'student' : student
    }
    return render(request,'Hod/views_student.html',context)

def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id=id)
    course = Courses.objects.all()
    session_Year =Session_Year.objects.all()


    context ={
        'student':student,
        'course' :course,
        'session_Year':session_Year
    }
    return render(request,'Hod/edit_student.html',context)

def UPDATE_STUDENT(request):
    if request.method =='POST':

        student_id =request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email = request.POST.get('email')
        username =request.POST.get('username')
        password =request.POST.get('password')
        adress = request.POST.get('adress')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')

        # use the attribute names create new name for 
        user =CustomUser.objects.get(id = student_id)
        # user.profile_pic =profile_pic 
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username

        if profile_pic !=None and profile_pic != "":
            user.profile_pic = profile_pic

        if password !=None and password != "":
            user.set_password(password)    
        user.save()

        student =Student.objects.get(admin= student_id)
        student.adress=adress
        student.gender=gender

        course =Courses.objects.get(id = course_id)
        student.course_id=course

        session_year =Session_Year.objects.get(id=session_id)
        student.session_id=session_year
        student.save()
        messages.success(request,'Record are succcefully')
        return redirect(VIEW_STUDENT)

    return render(request,'Hod/edit_student.html')

def DELETE_STUDENT(request,admin):
    student =CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'succefully deleted')
    return redirect(VIEW_STUDENT)

# write like this also
# def DELETE_STUDENT(request,id):
#     student =Student.objects.get(id=id)
#     student.delete()
#     messages.success(request,'succefully deleted')
#     return redirect(VIEW_STUDENT)

def ADD_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')

        course = Courses(
            name = course_name
        )
        course.save()
        messages.success(request,'succefully register new course')
        return redirect(ADD_COURSE)
    return render(request,'Hod/add_course.html')

def COURSE_VIEW(request):
    course = Courses.objects.all()
    context = {
        'course' : course
    }
    return render(request,'Hod/course_view.html',context)


def EIDT_COURSE(request,id):
    course =Courses.objects.get(id=id)
    context ={
        'course':course
    }
    return render(request,'Hod/course_edit.html',context)

def UPDATE_COURSE(request,id):
    course =Courses.objects.get(id=id)
    if request.method =='POST':
        # course_name =request.POST.get('course_name')
        # course.name= course_name
        #make lines to sort to write below code we can remove above the two lines
        course.name =request.POST.get('course_name')         
        course.save()
        return redirect(COURSE_VIEW)

    return render(request,'Hod/course_edit.html')


# def UPDATE_COURSE(request,id):
#     course = Courses.objects.get(id=id)
#     if request.method == 'POST':
#         course.name = request.POST.get('course_name')
#         course.save()
#         messages.success(request, 'Course updated successfully')
#         return redirect(COURSE_VIEW)
#     else:
#         context = {
#             'course': course
#         }
#         return render(request, 'Hod/course_edit.html', context)
 
def COURSE_DELETE(request,id):
    course =Courses.objects.get(id=id)
    course.delete()
    return redirect('course_view')

def ADD_STAFF(request):
    if request.method =='POST':
        profile_pic =request.FILES.get('profile_pic')
        first_name =request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email = request.POST.get('email')
        password =request.POST.get('password')
        adress=request.POST.get('adress')
        gender =request.POST.get('gender') 

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Email is already taken')
            return redirect(ADD_STAFF)
        
        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request,'email is already taken')
        else:
            user = CustomUser(
                profile_pic =profile_pic,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                user_type= 2
            )
            user.set_password(password)
            user.save()
            
            staff=Staff(
                admin=user,
                adress=adress, 
                gender=gender,
            )
            staff.save()
            messages.success(request,'staf are succefully added')
            return redirect('add_staff')
            # return redirect(VIEWS_STAFF)

    return render(request,'Hod/add_staff.html')

def VIEWS_STAFF(request):
    staff =Staff.objects.all()

    context ={
        'staff' : staff
    }
    return render(request,'Hod/staff_views.html',context)

def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id = id)
    context ={
        'staff' : staff
    }
    return render(request,'Hod/edit_staff.html',context)

def UPDATE_STAFF(request):
    if request.method =='POST':
        staff_id=request.POST.get('staff_id')
        profile_pic = request.POST.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POSt.get('last_name')
        email=request.POST.get('email')
        username =request.POST.get('username')
        password=request.POST.get('password')
        adress=request.POST.get('password')
        gender=request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username

        if profile_pic != None and profile_pic !="":
            user.profile_pic=profile_pic

        if password != None and password != '':
            user.set_password(password)
            user.save()

        staff =Staff.objects.get(admin = staff_id)
        staff.adress=adress
        staff.gender=gender
        staff.save()
        messages.success(request,'update succefully')
        return redirect(VIEWS_STAFF)

    return render(request,'Hod/edit_staff.html')

def HOD_VIEWS(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.warning(request,'staff succefully delete')
    return redirect(VIEWS_STAFF)