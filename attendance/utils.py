
from django.db.models import Count, Q
from .models import Attendance


def calculate_attendance_percentage(student, subject=None):

    records = Attendance.objects.filter(student=student)

    if subject is not None:
        records = records.filter(subject=subject)

    summary = records.aggregate(
        total=Count('id'),
        present=Count('id', filter=Q(status='PRESENT'))
    )

    total = summary['total']
    present = summary['present']

    if total == 0:
        return 0.0

    percentage = (present / total) * 100

    return round(percentage, 2)
