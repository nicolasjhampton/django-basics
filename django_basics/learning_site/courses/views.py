from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Course, Step
# Create your views here.

# def render_course(course):
#     return """
#     <li>
#         <h2>{title}</h2>
#         <p>{desc}</p>
#     </li>
#     """.format(title=course.title, desc=course.description)

# def get_courses(request):
#     courses = Course.objects.all()
#     return HttpResponse("""
#     <!doctype html>
#     <html>
#         <head></head>
#         <body>
#             <ul>
#                 {list}
#             </ul>
#         </body>
#     </html>
#     """.format(list="".join([render_course(c) for c in courses])))

def list_courses(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", context=dict(courses=courses))


def course_details(request, pk):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', { 'course': course })


def step_details(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', { 'step': step })
