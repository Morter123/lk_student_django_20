from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)  # Название курса
    description = models.TextField()  # Описание курса

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Связь с пользователем
    full_name = models.CharField(max_length=200)  # ФИО студента
    date_of_birth = models.DateField()  # Дата рождения
    courses = models.ManyToManyField(Course, through='Grade', related_name='students')  # Связь с курсами через оценки

    def __str__(self):
        return self.full_name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.FloatField(default=0)


    def __str__(self):
        return f'{self.student.full_name} - {self.course.name}: {self.grade}'
