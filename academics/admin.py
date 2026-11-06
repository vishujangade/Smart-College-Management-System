
from django.contrib import admin
from .models import AcademicYear, Department, Semester, Subject


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year_name', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_code')
    search_fields = ('department_name', 'department_code')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('semester_number', 'semester_name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject_code',
        'subject_name',
        'department',
        'semester',
        'credits',
    )
    search_fields = ('subject_code', 'subject_name')
    list_filter = ('department', 'semester')
