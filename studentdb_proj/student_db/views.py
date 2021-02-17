from django.shortcuts import render
from student_db.models import Student
# Create your views here.

def home_page(request):
    students = Student.objects.all()
    return render(request,'testapp/index.html',{'students':students})
