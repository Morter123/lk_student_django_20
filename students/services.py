from .models import Student

# Анализ успеваемости студента
def analyze_student_performance(student):
    grades = student.grades.all()  # Предположим, что у студента есть связанные оценки
    if not grades:
        return "No grades available"
    
    average_grade = sum(grade.value for grade in grades) / len(grades)
    return f"Average grade: {average_grade:.2f}"

# Анализ студентов по курсу
def analyze_by_course(course_name):
    students = Student.objects.filter(course=course_name)
    if not students:
        return {'error': 'No students found for this course'}
    
    analysis = {}
    for student in students:
        analysis[student.student_id] = analyze_student_performance(student)
    
    return analysis
