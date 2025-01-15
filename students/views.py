from django.shortcuts import render, get_object_or_404
from .models import Student
from django.db.models import Avg, Count
from .models import Grade, Course


def student_dashboard(request, id):  # Добавляем параметр id
    student = get_object_or_404(Student, pk=id)  # Получаем студента по ID
    grades = student.grade_set.all()  # Получаем все оценки для этого студента

    # Получаем все курсы студента через Grade
    courses = [grade.course for grade in grades]

    return render(request, 'students/dashboard.html', {
        'student': student,
        'courses': courses,
        'grades': grades
    })


def analysis_view(request):
    # Вычисляем средний балл по каждому курсу
    courses_with_avg = Course.objects.annotate(avg_grade=Avg('grade__grade'))

    return render(request, 'students/analysis.html', {'courses_with_avg': courses_with_avg})
