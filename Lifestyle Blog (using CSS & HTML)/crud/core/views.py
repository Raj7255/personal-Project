from django.shortcuts import render, redirect,get_object_or_404
from .models import Student 
from .forms import AddStudentForm



def index(request):
    Stu_data = Student.objects.all()
    return render(request, 'index.html', {'studata' : Stu_data})


def add_student(request):
    if request.method == 'POST':
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()  
            return redirect('home') 
        else:
            print(fm.errors)  
    else:
        fm = AddStudentForm()  
    return render(request, 'add_student.html', {'form': fm})



def delete_student(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=id)
        student.delete()
        return redirect('home')

     


def edit_student(request, id):
    stu = get_object_or_404(Student, id=id)
    if request.method == 'POST': 
        fm = AddStudentForm(request.POST, instance=stu)  
        if fm.is_valid():
            fm.save()  
            return redirect('home')  
        else:
            return render(request, 'edit_student.html', {'form': fm, 'stu': stu})
    else:
        fm = AddStudentForm(instance=stu) 
    return render(request, 'edit_student.html', {'form': fm, 'stu': stu})  


