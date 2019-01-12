from django.urls import path, re_path

from . import views

app_name = 'courses'

urlpatterns = [
    re_path(r'^$', views.list_courses, name='list'),
    re_path(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_details, name='step'),
    re_path(r'(?P<pk>\d+)/$', views.course_details, name='detail'),
]