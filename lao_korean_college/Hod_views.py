from django.shortcuts import render, redirect
from django.contrib import auth, messages
from app.models import CustomUser, Officer, Student, Teacher, SessionYear, Subject


def home(request):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    sessionYear = SessionYear.objects.all()
    officer = Officer.objects.all()

    student_count = len(student)
    teacher_count = len(teacher)
    sessionYear_count = len(sessionYear)
    officer_count = len(officer)

    dict = {
        'student_count': student_count,
        'teacher_count': teacher_count,
        'sessionYear_count': sessionYear_count,
        'officer_count': officer_count,
    }

    return render(request, 'Hod/home.html', context=dict)

# ----- For Officer -----
def addOfficer(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        officerID = request.POST.get('officerID')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
    
        if Officer.objects.filter(officerID=officerID).exists():
            messages.warning(request, 'This officer ID is already exist!')
            return redirect('add_officer')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This email is already exist!')
            return redirect('add_officer')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This username is already exist!')
            return redirect('add_officer')

        user = CustomUser(
            first_name = first_name, 
            last_name = last_name, 
            email = email, 
            username = username,
            profile_pic = profile_pic,
            user_type = 2,
        )
        user.set_password(password)
        user.save()

        officer = Officer(
            officerID = officerID,
            user = user,
            address = address,
            gender = gender,
        )
        officer.save()
        messages.success(request, 'Officer Are Successfully Added!')
        return redirect('add_officer')
    return render(request, 'Hod/addOfficer.html')

def viewOfficer(request):
    officer = Officer.objects.all()
    context = {
        'officer': officer,
    }
    return render(request, 'Hod/viewOfficer.html', context)

def editOfficer(request, id):
    officer = Officer.objects.get(id = id)

    context = {
        'officer': officer
    }
    return render(request, 'Hod/editOfficer.html', context )

def updateOfficer(request):
    if request.method == "POST":
        officer_id = request.POST.get('officer_id')
        profile_pic = request.FILES.get('profile_pic')
        officerID = request.POST.get('officerID')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id = officer_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic   
        
        user.save()

        officer = Officer.objects.get(user = officer_id)
        officer.officerID = officerID
        officer.address = address
        officer.gender = gender

        officer.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_officer')

    return render(request,'Hod/editOfficer.html')

def deleteOfficer(request, user):
    officer = CustomUser.objects.get(id = user)
    officer.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_officer')

# --------- For Teacher ---------
def addTeacher(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        teacherID = request.POST.get('teacherID')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if Teacher.objects.filter(teacherID=teacherID).exists():
            messages.warning(request, 'This teacher ID is already exist!')
            return redirect('add_teacher')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This email is already exist!')
            return redirect('add_teacher')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This username is already exist!')
            return redirect('add_teacher')

        user = CustomUser(
            first_name = first_name, 
            last_name = last_name, 
            email = email, 
            username = username,
            profile_pic = profile_pic,
            user_type = 3,
        )
        user.set_password(password)
        user.save()

        teacher = Teacher(
            teacherID = teacherID,
            user = user,
            address = address,
            gender = gender,
        )
        teacher.save()
        messages.success(request, 'Teacher Are Successfully Added!')
        return redirect('add_teacher')

    return render(request, 'Hod/addTeacher.html')

def viewTeacher(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher': teacher
    }
    return render(request, 'Hod/viewTeacher.html', context)

def editTeacher(request, id):
    teacher = Teacher.objects.get(id = id)

    context = {
        'teacher':teacher
    }
    return render(request,'Hod/editTeacher.html',context)

def updateTeacher(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        profile_pic = request.FILES.get('profile_pic')
        teacherID = request.POST.get('teacherID')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id = teacher_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic   
        user.save()

        teacher = Teacher.objects.get(user = teacher_id)

        teacher.teacherID = teacherID
        teacher.address = address
        teacher.gender = gender

        teacher.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_teacher')

    return render(request,'Hod/editTeacher.html')

def deleteTeacher(request, user):
    teacher = CustomUser.objects.get(id = user)
    teacher.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_teacher')

# ----- For Student -----
def addStudent(request):
    sessionYear = SessionYear.objects.all()

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        studentID = request.POST.get('studentID')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        sessionYearID = request.POST.get('session_year_id')
        year = request.POST.get('year')
        part = request.POST.get('part')

        if Student.objects.filter(studentID=studentID).exists():
            messages.warning(request, 'This student ID is already exist!')
            return redirect('add_student')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This email is already exist!')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This username is already exist!')
            return redirect('add_student')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=4,
            )
            user.set_password(password)
            user.save()

            sessionYear = SessionYear.objects.get(id=sessionYearID)
            student = Student(
                user=user,
                studentID=studentID,
                address=address,
                gender=gender,
                sessionYearID=sessionYear,
                year = year,
                part = part,
            )
            student.save()
            messages.success(request, user.first_name + ' ' +
                             user.last_name + ' Is Successfully Added!')
            return redirect('add_student')

    context = {
        'sessionYear': sessionYear,
    }

    return render(request, 'Hod/addStudent.html', context)

def viewStudent(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'Hod/viewStudent.html', context)

def editStudent(request, id):
    students = Student.objects.filter(id = id)
    sessionYear = SessionYear.objects.all()

    context = {
        'students': students,
        'sessionYear': sessionYear,
    }
    return render(request, 'Hod/editStudent.html', context)

def updateStudent(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        studentID = request.POST.get('studentID')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(user = student_id)
        sessionYear = SessionYear.objects.get(id = session_year_id)
        student.studentID = studentID
        student.address = address
        student.gender = gender
        student.sessionYearID = sessionYear
        student.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_student')

def deleteStudent(request, user):
    student = CustomUser.objects.get(id = user)
    student.delete()
    messages.success(request, 'Successfully Deleted!')
    return redirect('view_student')

# ----- For Session Year -----
def addSessionYear(request):
    if request.method == 'POST':
        sessionYear = request.POST.get('sessionYear')
        sessionYear = SessionYear(
            sessionYear=sessionYear,
        )
        sessionYear.save()
        messages.success(request, 'Session Year Are Successfully Added!')
        return redirect('add_sessionYear')

    return render(request, 'Hod/addSessionYear.html')

def viewSessionYear(request):
    sessionYear = SessionYear.objects.all()
    context = {
        'sessionYear': sessionYear,
    }

    return render(request, 'Hod/viewSessionYear.html', context)

def editSessionYear(request, id):
    sessionYear = SessionYear.objects.get(id = id)
    context = {
        'sessionYear': sessionYear,
    }
    return render(request, 'Hod/editSessionYear.html', context)

def updateSessionYear(request):
    if request.method == 'POST':
        year = request.POST.get('sessionYear')
        sessionYear_id = request.POST.get('sessionYear_id')

        sessionYear = SessionYear.objects.get(id = sessionYear_id)
        sessionYear.sessionYear = year
        sessionYear.save()

        messages.success(request, 'Session Year Are Successfully Updated!')
        # return redirect('/Hod/SessionYear/Edit/'+sessionYear_id+'/')
        return redirect('view_sessionYear')

def deleteSessionYear(request, id):
    sessionYear = SessionYear.objects.get(id = id)
    sessionYear.delete()
    messages.success(request, 'Session Year Are Successfully Deleted!')
    return redirect('view_sessionYear')

# ------------ For Subject -----------------
def addSubject(request):
    session_year = SessionYear.objects.all()
    teachers = Teacher.objects.all()
    
    context = {
        'sessionYear':session_year,
        'teachers':teachers,
    }
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        year = request.POST.get('year')
        teacherID = request.POST.get('teacherID')
        sessionYearID = request.POST.get('sessionYearID')

        teacher = Teacher.objects.get(id=teacherID)
        sessionYear = SessionYear.objects.get(id=sessionYearID)
        subject = Subject(
            subject = subject_name,
            year = year,
            teacherID = teacher,
            sessionYearID = sessionYear,
        )
        subject.save()
        messages.success(request, 'Subject is Successfully Added!')
        return redirect('view_subject')

    return render(request, 'Subject/addSubject.html', context)

def viewSubject(request):
    subject = Subject.objects.all()

    context = {
        'subject':subject,
    }
    return render(request, 'Subject/viewSubject.html', context)

def deleteSubject(request, id):
    subject = Subject.objects.get(id = id)
    subject.delete()
    messages.success(request, 'Subject is Successfully Deleted!')
    return redirect('view_subject')

def editSubject(request, id):
    subject = Subject.objects.filter(id = id)
    teacher = Teacher.objects.all()
    sessionYear = SessionYear.objects.all()

    context = {
        'subject': subject,
        'teacher': teacher,
        'sessionYear': sessionYear,
    }
    return render(request, 'Subject/editSubject.html', context)

def updateSubject(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        year = request.POST.get('year')
        teacherID = request.POST.get('teacherID')
        sessionYearID = request.POST.get('sessionYearID')

        teacher = Teacher.objects.get(id = teacherID)
        sessionYear = SessionYear.objects.get(id = sessionYearID)

        subject = Subject.objects.get(id = subject_id)
        subject.subject = subject_name
        subject.teacherID = teacher
        subject.sessionYearID = sessionYear
        subject.year = year
        subject.created_at = subject.updated_at
        subject.save()
        messages.success(request, 'Subject is Successfully Udated!')
        return redirect('view_subject')

