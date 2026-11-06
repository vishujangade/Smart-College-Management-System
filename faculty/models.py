
from django.conf import settings
from django.db import models


class Faculty(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='faculty_profile'
    )

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.CharField(max_length=100)

    designation = models.CharField(max_length=100)

    qualification = models.CharField(max_length=150)

    joining_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"
