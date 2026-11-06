
from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'subject',
        'faculty',
        'date',
        'status',
    )

    list_filter = (
        'date',
        'status',
        'subject',
        'faculty',
    )

    search_fields = (
        'student__usn',
        'student__user__first_name',
        'student__user__last_name',
        'subject__subject_name',
    )

    date_hierarchy = 'date'

    ordering = ('-date',)
