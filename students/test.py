from django.test import TestCase, Client
from django.urls import reverse
from django.test import TestCase
from students.models import Course, Student, Grade
from django.contrib.auth.models import User


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="Математика", description="Курс по математике")

    def test_course_creation(self):
        self.assertEqual(self.course.name, "Математика")
        self.assertEqual(self.course.description, "Курс по математике")


class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.student = Student.objects.create(
            user=self.user, full_name="Иван Иванов", date_of_birth="2000-01-01")

    def test_student_creation(self):
        self.assertEqual(self.student.full_name, "Иван Иванов")
        self.assertEqual(str(self.student), "Иван Иванов")


class GradeModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="Математика", description="Курс по математике")
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.student = Student.objects.create(
            user=self.user, full_name="Иван Иванов", date_of_birth="2000-01-01")
        self.grade = Grade.objects.create(
            student=self.student, course=self.course, grade=85.0)

    def test_grade_creation(self):
        self.assertEqual(self.grade.grade, 85.0)
        self.assertEqual(str(self.grade), "Иван Иванов - Математика: 85.0")


class StudentDashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.student = Student.objects.create(
            user=self.user, full_name="Иван Иванов", date_of_birth="2000-01-01")
        self.course = Course.objects.create(
            name="Математика", description="Курс по математике")
        self.grade = Grade.objects.create(
            student=self.student, course=self.course, grade=95.0)
        self.client.login(username="testuser", password="password")

    def test_dashboard_view(self):
        response = self.client.get(
            reverse("dashboard", args=[self.student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "students/dashboard.html")
        self.assertContains(response, "Иван Иванов")
        self.assertContains(response, "Математика")
        self.assertContains(response, "95.0")


class StudentAnalysisViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.student = Student.objects.create(
            user=self.user, full_name="Иван Иванов", date_of_birth="2000-01-01")
        self.course = Course.objects.create(
            name="Математика", description="Курс по математике")
        self.grade = Grade.objects.create(
            student=self.student, course=self.course, grade=95.0)

    def test_analysis_view(self):
        response = self.client.get(reverse("analysis"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "students/analysis.html")
        self.assertContains(response, "Математика")
        self.assertContains(response, "Средний балл")
        self.assertContains(response, "95.0")
