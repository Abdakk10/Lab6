from django.shortcuts import render, redirect
from .models import Student, Course

def students(request):
    students_list = Student.objects.all()
    return render(request, 'students/students.html', {'students_list': students_list})

def add_student(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST['name']
        age = request.POST['age']
        # Add more fields as required
        student = Student.objects.create(name=name, age=age)
        return redirect('students')
    return render(request, 'students/add_student.html')

def courses(request):
    courses_list = Course.objects.all()
    return render(request, 'students/courses.html', {'courses_list': courses_list})

def add_course(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST['name']
        # Add more fields as required
        course = Course.objects.create(name=name)
        return redirect('courses')
    return render(request, 'students/add_course.html')

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    not_registered_courses = Course.objects.exclude(students=student)
    if request.method == 'POST':
        course_id = request.POST['course']
        course = Course.objects.get(pk=course_id)
        student.courses.add(course)
    return render(request, 'students/details.html', {'student': student, 'not_registered_courses': not_registered_courses})

