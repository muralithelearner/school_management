from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Courses,Session_Year,CustomUser,Student,Staff,Subject,Staff
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count =Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count =Courses.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male =Student.objects.filter(gender="Male").count()
    student_gender_female = Student.objects.filter(gender="Female").count()

    context = {
        'student_count' : student_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subject_count' : subject_count,
        'student_gender_male' : student_gender_male,
        'student_gender_female' : student_gender_female

    }
    return render(request,'Hod/home.html',context)

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

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student =Student.objects.all()

    context ={
        'student' : student
    }
    return render(request,'Hod/views_student.html',context)

@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
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
@login_required(login_url='/')
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

@login_required(login_url='/')
def COURSE_VIEW(request):
    course = Courses.objects.all()
    context = {
        'course' : course
    }
    return render(request,'Hod/course_view.html',context)


@login_required(login_url='/')
def EIDT_COURSE(request,id):
    course =Courses.objects.get(id=id)
    context ={
        'course':course
    }
    return render(request,'Hod/course_edit.html',context)

@login_required(login_url='/')
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

@login_required(login_url='/')
def COURSE_DELETE(request,id):
    course =Courses.objects.get(id=id)
    course.delete()
    return redirect('course_view')

@login_required(login_url='/')
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

@login_required(login_url='/')
def VIEWS_STAFF(request):
    staff =Staff.objects.all()

    context ={
        'staff' : staff
    }
    return render(request,'Hod/staff_views.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id = id)
    context ={
        'staff' : staff
    }
    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')
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

@login_required(login_url='/')
def HOD_VIEWS(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.warning(request,'staff succefully delete')
    return redirect(VIEWS_STAFF)

@login_required(login_url='/')
def ADD_SUBJECT(request):
    course =Courses.objects.all()
    staff = Staff.objects.all()

    if request.method =='POST':
        subject_name =request.POST.get('subject_name')
        course_id =request.POST.get('course_id')
        staff_id =request.POST.get('staff_id')

        course =Courses.objects.get(id=course_id)
        staff =Staff.objects.get(id=staff_id)
        
        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff
        )
        subject.save()
        messages.success(request,'subject add succefully')
        return redirect(ADD_SUBJECT)

    context ={
        'course' : course,
        'staff' : staff
    }
    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject =Subject.objects.all()


    context ={
        'subject' : subject
    }
    return render(request,'Hod/view_subject.html',context)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id=id)
    course = Courses.objects.all()
    staff =Staff.objects.all()

    context ={
        'subject' : subject,
        'course' : course,
        'staff' : staff
    }
    return render(request,'Hod/edit_subject.html',context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        subject_id =request.POST.get('subject_id')
        subject_name =request.POST.get('subject_name')
        course_id =request.POST.get('course_id')
        staff_id =request.POST.get('staff_id')
        
        course = Courses.objects.get(id=course_id)
        staff =Staff.objects.get(id=staff_id)

        subject =Subject.objects.get(id=subject_id)
        subject.name=subject_name
        subject.course=course
        subject.staff=staff
        subject.save()
        messages.success(request,'update succefully')
        return redirect('view_subject')

    return render(request,'Hod/edit_subject.html')

@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.warning(request,'succefully delete subject')
    return redirect(VIEW_SUBJECT)

def ADD_SESSION(request):
    if request.method == 'POST':
        session_start =request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session_Year(
            session_start =session_start,
            session_end = session_end
        )
        session.save()
        messages.success(request,'session  add succefully')
        return redirect(ADD_SESSION)
    return render(request,'Hod/add_session.html')

def VIEW_SESSION(request):
    session = Session_Year.objects.all()

    context ={
        'session': session
    }
    return render(request,'Hod/view_session.html',context)


def EDIT_SESSION(request,id):
    session = Session_Year.objects.filter(id=id)

    context ={
        'session': session
    }
    return render(request,'Hod/edit_session.html',context)

from django.shortcuts import get_object_or_404

def UPDATE_SESSION(request):
    if request.method =="POST":
        session_id=request.POST.get('session_id')
        session_start =request.POST.get('session_start')
        session_end= request.POST.get('session_end')

        session = Session_Year.objects.get(id=session_id)
        session.session_start=session_start
        session.session_end=session_end
        session.save()
        messages.success(request,'session update succefully')
        return redirect(VIEW_SESSION)

    return redirect(request,'Hod/edit_session.html')


def DELETE_SESSION(request,id):
    session =Session_Year.objects.get(id=id)
    session.delete()
    messages.warning(request,'delete session sucessfully')
    return redirect(VIEW_SESSION)

def STAFF_SEND_NOTIFICATIONS(request):
    staff = Staff.objects.all()

    context ={
        'staff' : staff
    }
    return render(request,'Hod/staff_notifications.html',context)