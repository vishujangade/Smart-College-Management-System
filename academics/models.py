
from django.db import models


class AcademicYear(models.Model):

    year_name = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.year_name


class Department(models.Model):

    department_name = models.CharField(max_length=100, unique=True)
    department_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.department_name


class Semester(models.Model):

    semester_number = models.PositiveSmallIntegerField(unique=True)
    semester_name = models.CharField(max_length=50)

    def __str__(self):
        return self.semester_name


class Subject(models.Model):

    subject_code = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=150)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )

    credits = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"

