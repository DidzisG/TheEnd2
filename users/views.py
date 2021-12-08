from django.shortcuts import render

from .models import StudentModel
from .forms import StudentForm

users = []


def students(request):
    users = StudentModel.objects.all()
    context = {
        'users': users,
    }

    return render(
        request,
        template_name='students.html',
        context=context,
    )


def add_student(request):

    form = StudentForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = StudentModel(
                name=form.cleaned_data['name'],
                grades=form.cleaned_data['grades'],
            )

            user.save()

            context = {
                'user': user,
            }

            return render(
                request,
                template_name='student.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_student.html',
        context=context,
    )


def get_student(request, name_id):

    user = StudentModel.objects.get(id=name_id)

    context = {
    'user': user,
    }

    return render(
        request,
        template_name= 'student.html',
        context= context,

    )

