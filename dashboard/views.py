from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from students.models import Student
from faculty.models import Faculty
from academics.models import Subject
from attendance.models import Attendance
from examinations.models import Examination, Marks


@login_required
def dashboard_home(request):

    user = request.user

    if user.is_superuser or user.role == 'ADMIN':
        role = 'Admin'
    elif user.role == 'FACULTY':
        role = 'Faculty'
    else:
        role = 'Student'

    context = {
        'role': role,
        'total_students': Student.objects.count(),
        'total_faculty': Faculty.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_attendance': Attendance.objects.count(),
        'total_examinations': Examination.objects.count(),
        'total_marks': Marks.objects.count(),
    }

    return render(request, 'dashboard/home.html', context)