from django.shortcuts import render
from .models import teachers,students

# Create your views here.

def display_data(request):
    selected_student = None
    selected_teacher = None
    teacher = teachers.objects.all()
    student = students.objects.all()

    if request.method =='POST':
        teachers_id = request.POST.get('teacher')
        students_id = request.POST.get('student')
        if teachers_id:
         selected_teacher  = teachers.objects.get(id = teachers_id)
        elif students_id:
         selected_student  = students.objects.get(id= students_id)

    context = {
            'selected_teacher':selected_teacher,
            'selected_student':selected_student,
            'teacher':teacher,
            'student':student,
         }

    return render(request,'m2mapp/index.html',context)
