from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

# Create your tests here.
from .models import Course, Step


class CourseModelTests(TestCase):

    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regex",
            description="Learn to write regex"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)



class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Regex",
            description="Learn to write regex"
        )
        self.course2 = Course.objects.create(
            title="Python Testing",
            description="Test everything"
        )
        self.step = Step.objects.create(
            title="Begin and end",
            description="Using ^ and $ to write regex",
            course=self.course
        )

    def test_course_list_view(self):
        res = self.client.get(reverse('courses:list'))
        self.assertEqual(res.status_code, 200)
        self.assertIn(self.course, res.context['courses'])
        self.assertIn(self.course2, res.context['courses'])
        self.assertTemplateUsed(res, 'courses/course_list.html')
        self.assertContains(res, self.course.title)

    def test_course_detail_view(self):
        res = self.client.get(reverse('courses:detail', kwargs={
            "pk": self.course.pk
        }))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.course, res.context['course'])