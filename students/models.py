
from django.conf import settings
from django.db import models


class Student(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )

    usn = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    semester = models.PositiveSmallIntegerField()
    admission_year = models.PositiveSmallIntegerField()
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usn} - {self.user.get_full_name()}"

