"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  #this is for media

from .import Hod_views, views,staff_views,student_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.BASE,name='base'),

    # Login_page
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='doLogout'),

    # THis is Hod pannel
    path('Hod/Home',Hod_views.HOME,name='hod/home'),

    #profile
    path('profile',views.PROFILE,name='profile'),
    # path('profile/update/<id>',views.PROFILE_UPDATE,name='profile/update')
    path('profile/update',views.PROFILE_UPDATE,name='profile/update'),
    path('hod/student/add',Hod_views.ADD_STUDENT,name='add_student'),
    path('hod/student/views',Hod_views.VIEW_STUDENT,name='views_student'),
    path('hod/student/edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),
    path('hod/student/update',Hod_views.UPDATE_STUDENT,name='update_student'),
    path('hod/student/delete/<str:admin>',Hod_views.DELETE_STUDENT,name='student_delete'),


    path('hod/staff/add',Hod_views.ADD_STAFF,name='add_staff'),
    path('hod/staff/views',Hod_views.VIEWS_STAFF,name="views_staff"),
    path('hod/staff/edit/<str:id>',Hod_views.EDIT_STAFF,name="edit_staff"),
    path('hod/staff/update',Hod_views.UPDATE_STAFF,name='update_staff'),
    path('hod/staff/delete/<str:admin>',Hod_views.HOD_VIEWS,name='staff_delete'),

    path('hod/course/add_course',Hod_views.ADD_COURSE,name='add_course'),
    path('hod/course/view',Hod_views.COURSE_VIEW,name='course_view'),
    path('hod/course/edit/<str:id>',Hod_views.EIDT_COURSE,name='edit_course'),
    # path('hod/course/update/',Hod_views.UPDATE_COURSE,name='update_course'),
    path('hod/course/update/<int:id>/',Hod_views.UPDATE_COURSE,name='update_course'),
    path('hod/course/delete/<int:id>',Hod_views.COURSE_DELETE,name="course_delete"),


    path('hod/subject/add',Hod_views.ADD_SUBJECT,name='add_subject'),
    path('hod/subject/view',Hod_views.VIEW_SUBJECT,name='view_subject'),
    path('hod/subject/edit/<int:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
    path('hod/subject/update',Hod_views.UPDATE_SUBJECT,name="update_subject"),
    path('hod/subject/delete/<int:id>',Hod_views.DELETE_SUBJECT,name="delete_subject"),

    path('hod/session/add',Hod_views.ADD_SESSION,name='add_session'),
    path('hod/session/view',Hod_views.VIEW_SESSION,name='view_session'),
    path('hod/session/edit/<int:id>',Hod_views.EDIT_SESSION,name='edit_session'),
    path('hod/session/update',Hod_views.UPDATE_SESSION,name='update_session'),
    path('hod/session/delete/<int:id>',Hod_views.DELETE_SESSION,name='delete_session'),


    # staff login
    path('staff/home',staff_views.STAFF_HOME,name='staff_home')

    # write like this also
    # path('hod/student/delete/<str:id>',Hod_views.DELETE_STUDENT,name='student_delete')




]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)  #this for media 
