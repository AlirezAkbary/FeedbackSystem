from django.shortcuts import render
from .models import Course
from .forms import CourseCreateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from Professor.models import Professor
from Student.models import Student
from .models import Course
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q

@login_required
def AddCourse(request):
    if request.method == "POST":### Need Checks for wrong inputs

        post_dict = dict(request.POST.lists())

        CourseForm = Course(CourseID=int(post_dict['CourseID'][0]))
        CourseForm.GroupID = int(post_dict['GroupID'][0])
        CourseForm.Name = post_dict['Name'][0]
        CourseForm.save()

        self_user = Professor.objects.get(ProfID=int(request.user.username))
        CourseForm.Professor.add(self_user)

        new_professors = post_dict['new']

        for i in new_professors:
            if i != '':
                current_prof = get_object_or_404(Professor, ProfID=int(i))
                if current_prof is not None:
                    CourseForm.Professor.add(current_prof)
        return HttpResponseRedirect(reverse('professor', kwargs={'id':int(request.user.username)}))
    else:
        course_form = CourseCreateForm()
    return render(request, 'course/CourseForm.html', {'course_form':course_form})
# Create your views here.

def SearchCourse(request):

    query = request.GET.get('q')
    user = request.user.username
    user = Student.objects.filter(
        Q(StudentID=user)
    )

    object_list = Course.objects.filter(
        Q(Name__icontains=query)
    )
    professor_name_strings = []
    objects = []
    for o in object_list:
        prof = o.Professor.all()

        s = ""
        for i in range(len(prof)):
            s += prof[i].FirstName + " " + prof[i].LastName
        professor_name_strings.append(s)
    for o in range(len(object_list)):
        objects.append([object_list[o], o])

    context = {
        'object': object_list,
        'user':user[0],
        'names':professor_name_strings,
        'iter' : 0
    }



    return render(request, 'Course/Course_Search.html', context)

def joinCourse(request, id, group):
    object = Course.objects.filter(
        Q(CourseID=id, GroupID = group)

    )
    user = request.user.username
    user = Student.objects.filter(
        Q(StudentID=user)
    )
    context = {
        "object":object[0],
        "user":user[0]
    }

    object[0].Student.add(user[0])

    print(user[0].course_set.all())
    print(object[0].Student.all())





    return render(request, 'Course/joinCourse.html', context)


@login_required
def courseHome(request, cid, gid):
    if Professor.objects.get(ProfID=int(request.user.username)) != None:
        return courseHomeProfView(request, cid, gid)
    return courseHomeStudentView(request, cid, gid)


def courseHomeProfView(request, cid, gid):
    return render(request, 'professor/ProfessorCourseView.html', {})

def courseHomeStudentView(request, cid, gid):
    pass