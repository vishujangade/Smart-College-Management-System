
from django.contrib import admin
from .models import Examination, Marks


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):

    list_display = (
        'exam_name',
        'exam_type',
        'subject',
        'exam_date',
        'maximum_marks',
        'passing_marks',
    )

    list_filter = ('exam_type', 'exam_date', 'subject')

    search_fields = ('exam_name', 'subject__subject_name')


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'examination',
        'marks_obtained',
        'result_status',
        'faculty',
    )

    list_filter = ('examination', 'faculty')

    search_fields = (
        'student__usn',
        'student__user__first_name',
        'student__user__last_name',
    )
