from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Project
from models import Position

from matching_system_project.forms import UserForm, UserProfileForm


from matching_system_project.forms import ProjectForm, PositionForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from models import Application
from django.contrib.auth.models import User


from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def index(request):

    context = RequestContext(request)
    position_list = Position.objects.all()
    position_dict ={'positions':position_list}
    return render_to_response('matching_system_project/index.html', position_dict, context)

    # return HttpResponse('<h1>Projects System</h1>' +
    #                     '<a href="/projects">View Projects</a>')

def projects(request):
    return HttpResponse("PROJECTS IN YOUR FACE MOFO")

def project(request, project_name_url):
    context = RequestContext(request)
    project_name = project_name_url.replace('_', ' ' )

    project = Project.objects.get(url=project_name_url)

    project_name = project_name_url.replace('_', ' ' )

    # position lis

    position_list = Position.objects.all()
    print position_list

    position_dict ={'positions':position_list}

    context_dict = {'project_name': project_name}
    context_dict = {
        'projectName': project.projectName,
        'description': project.description,
        'position_list': position_list,

    }

    try:

        context_dict['project'] = project
    except Project.DoesNotExist:
        # We get here if we didn't find the specified project.
        # Don't do anything - the template displays the "no project" message for us.
        pass

    #return HttpResponse("I AM A PROJECT")
    return render_to_response('matching_system_project/project.html', context_dict, context)



def add_project(request):
    context = RequestContext(request)
    if request.method == 'POST':

        # this is returning an error when we add a new project so I commented it
        # form = ProjectForm(request.POST, user=request.user)

        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = ProjectForm()

    return render_to_response('matching_system_project/add_project.html', {'form': form}, context)

def add_position(request):

    context = RequestContext(request)
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():

            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = PositionForm()
    return render_to_response('matching_system_project/add_position.html', {'form': form}, context)

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.first_name = user_form.first_name
            user.last_name = user_form.last_name

            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'matching_system_project/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('matching_system_project/login.html', {}, context)

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def applist(request):

    context = RequestContext(request)
    proj_list=Project.objects.all()
    pos_list=Position.objects.all()
    app_list =Application.objects.all()
    us_list=User.objects.all()


    context_dict={
     'projects':proj_list,
     'positions':pos_list,
     'applications':app_list,
     #'users':us_list,
                }
    return render_to_response('matching_system_project/applist.html', context_dict, context)