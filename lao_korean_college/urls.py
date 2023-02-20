"""lao_korean_college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views, Hod_views, Teacher_views, Student_views
from blogs.views import viewBlog, blogDetial, editBlog, deleteBlog, updateBlog, addBlog
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Login Path
    path('', views.login, name='login'),
    path('dologin/', views.dologin, name='dologin'),
    path('dologout/', views.dologout, name='dologout'),

    # ------ For Hod panel url ------
    path('Hod/Home/', Hod_views.home, name='hod_home'),
    # For Officer Path
    path('Hod/Officer/Add/', Hod_views.addOfficer, name='add_officer'),
    path('Hod/Officer/View/', Hod_views.viewOfficer, name='view_officer'),
    path('Hod/Officer/Edit/<str:id>/', Hod_views.editOfficer, name='edit_officer'),
    path('Hod/Officer/Update/', Hod_views.updateOfficer, name='update_officer'),
    path('Hod/Officer/Delete/<str:user>/', Hod_views.deleteOfficer, name='delete_officer'),
    # For Teacher Path
    path('Hod/Teacher/Add/', Hod_views.addTeacher, name='add_teacher'),
    path('Hod/Teacher/View/', Hod_views.viewTeacher, name='view_teacher'),
    path('Hod/Teacher/Edit/<str:id>/', Hod_views.editTeacher, name='edit_teacher'),
    path('Hod/Teacher/Update/', Hod_views.updateTeacher,name='update_Teacher'),
    path('Hod/Teacher/Delete/<str:user>', Hod_views.deleteTeacher,name='delete_teacher'),
    # For Student Path
    path('Hod/Student/Add/', Hod_views.addStudent, name='add_student'),
    path('Hod/Student/View/', Hod_views.viewStudent, name='view_student'),
    path('Hod/Student/Edit/<str:id>/', Hod_views.editStudent, name='edit_student'),
    path('Hod/Student/Update/', Hod_views.updateStudent, name='update_student'),
    path('Hod/Student/Delete/<str:user>/', Hod_views.deleteStudent, name='delete_student'),
    # For Session Year Path
    path('Hod/Session_year/Add/', Hod_views.addSessionYear, name='add_sessionYear'),
    path('Hod/Session_year/View/', Hod_views.viewSessionYear, name='view_sessionYear'),
    path('Hod/Session_year/Edit/<str:id>/', Hod_views.editSessionYear, name='edit_sessionYear'),
    path('Hod/Session_year/Update/', Hod_views.updateSessionYear, name='update_sessionYear'),
    path('Hod/Session_year/Delete/<str:id>/', Hod_views.deleteSessionYear, name='delete_sessionYear'),

    # ------ For Teacher paner -------
    path('Teacher/Home/', Teacher_views.home, name='teacher_home'),

    # ------ For Student paner -------
    path('Student/Home/', Student_views.home, name='student_home'),

    # ------ For Blog App ---------------
    path('Hod/Blog/Add/', addBlog, name='add_blog'),
    path('Hod/Blog/View/', viewBlog, name='view_blog'),
    path('Hod/Blog/Detial/<str:id>/', blogDetial, name='blog_detial'),
    path('Hod/Blog/Edit/ <str:id>/', editBlog, name='edit_blog'),
    path('Hod/Blog/Update/', updateBlog, name='update_blog'),
    path('Hod/Blog/Delete/ <int:id>/', deleteBlog, name='delete_blog'),

    # -------- Subject path -----------
    path('Hod/Subject/Add/', Hod_views.addSubject, name='add_subject'),
    path('Hod/Subject/View/', Hod_views.viewSubject, name='view_subject'),
    path('Hod/Subject/Delete/ <str:id>', Hod_views.deleteSubject, name='delete_subject'),
    path('Hod/Subject/Edit/ <str:id>/', Hod_views.editSubject, name='edit_subject'),
    path('Hod/Subject/Update/', Hod_views.updateSubject, name='update_subject'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
