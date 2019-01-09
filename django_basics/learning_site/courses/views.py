from django.shortcuts import render
from django.http import HttpResponse

from .models import Course
# Create your views here.

def render_course(course):
    return """
    <li>
        <h2>{title}</h2>
        <p>{desc}</p>
    </li>
    """.format(title=course.title, desc=course.description)

def get_courses(request):
    courses = Course.objects.all()
    return HttpResponse("""
    <!doctype html>
    <html>
        <head></head>
        <body>
            <ul>
                {list}
            </ul>
        </body>
    </html>
    """.format(list="".join([render_course(c) for c in courses])))

