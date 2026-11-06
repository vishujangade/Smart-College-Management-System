from collections import defaultdict
from examinations.models import Marks


def get_exam_rankings(examination):
    """
    Calculate student rankings for one examination.
    Students with equal marks receive the same rank.
    """

    records = (
        Marks.objects
        .filter(examination=examination)
        .select_related('student', 'student__user', 'examination')
        .order_by('-marks_obtained', 'student__usn')
    )

    rankings = []
    previous_marks = None
    current_rank = 0

    for position, record in enumerate(records, start=1):
        if record.marks_obtained != previous_marks:
            current_rank = position
            previous_marks = record.marks_obtained

        maximum = examination.maximum_marks
        percentage = (
            (record.marks_obtained / maximum) * 100
            if maximum > 0 else 0
        )

        rankings.append({
            'rank': current_rank,
            'usn': record.student.usn,
            'student_name': record.student.user.get_full_name(),
            'marks_obtained': record.marks_obtained,
            'maximum_marks': maximum,
            'percentage': round(percentage, 2),
            'status': record.result_status,
        })

    return rankings


def get_overall_rankings():
    """
    Calculate overall rankings using all available examination marks.
    """

    records = (
        Marks.objects
        .select_related('student', 'student__user', 'examination')
        .all()
    )

    student_totals = defaultdict(
        lambda: {'obtained': 0, 'maximum': 0, 'student': None}
    )

    for record in records:
        student_id = record.student_id
        student_totals[student_id]['obtained'] += record.marks_obtained
        student_totals[student_id]['maximum'] += record.examination.maximum_marks
        student_totals[student_id]['student'] = record.student

    sorted_students = sorted(
        student_totals.values(),
        key=lambda item: (
            -item['obtained'],
            item['student'].usn
        )
    )

    rankings = []
    previous_percentage = None
    current_rank = 0

    for position, item in enumerate(sorted_students, start=1):
        maximum = item['maximum']
        percentage = (
            (item['obtained'] / maximum) * 100
            if maximum > 0 else 0
        )
        percentage = round(percentage, 2)

        if percentage != previous_percentage:
            current_rank = position
            previous_percentage = percentage

        student = item['student']

        rankings.append({
            'rank': current_rank,
            'usn': student.usn,
            'student_name': student.user.get_full_name(),
            'total_marks': item['obtained'],
            'maximum_marks': maximum,
            'percentage': percentage,
        })

    return rankings