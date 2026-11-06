
from django.db import models
from students.models import Student
from faculty.models import Faculty
from academics.models import Subject


class Examination(models.Model):

    EXAM_TYPES = [
        ('INTERNAL', 'Internal Assessment'),
        ('MIDTERM', 'Midterm Examination'),
        ('FINAL', 'Final Examination'),
        ('PRACTICAL', 'Practical Examination'),
    ]

    exam_name = models.CharField(max_length=100)

    exam_type = models.CharField(
        max_length=20,
        choices=EXAM_TYPES
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    exam_date = models.DateField()

    maximum_marks = models.PositiveSmallIntegerField(default=100)

    passing_marks = models.PositiveSmallIntegerField(default=35)

    def __str__(self):
        return f"{self.exam_name} - {self.subject.subject_name}"


class Marks(models.Model):

    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE,
        related_name='marks_records'
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    marks_obtained = models.FloatField()

    remarks = models.CharField(
        max_length=255,
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['examination', 'student'],
                name='unique_student_exam_marks'
            )
        ]

    @property
    def result_status(self):
        if self.marks_obtained >= self.examination.passing_marks:
            return "PASS"
        return "FAIL"

    def __str__(self):
        return f"{self.student.usn} - {self.marks_obtained}"
