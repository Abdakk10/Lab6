from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('add/', views.add_student, name='add_student'),
    path('courses/', views.courses, name='courses'),
    path('courses/add/', views.add_course, name='add_course'),
    path('details/<int:student_id>/', views.details, name='details'),
]
