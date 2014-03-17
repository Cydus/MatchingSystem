from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Project
from models import Position

from matching_system_project.forms import UserForm, UserProfileForm


from matching_system_project.forms import ProjectForm, PositionForm

from django.http import HttpResponse

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

    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the project title to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the title.
    project_name = project_name_url.replace('_', ' ' )

    project = Project.objects.get(url=project_name_url)

    # Change underscores in the project title to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the title.
    project_name = project_name_url.replace('_', ' ' )

    # position lis

    position_list = Position.objects.all()
    print position_list

    position_dict ={'positions':position_list}

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the title of the project passed by the user.
    context_dict = {'project_name': project_name}
    context_dict = {
        'projectName': project.projectName,
        'description': project.description,
        'position_list': position_list,

    }

    try:
        # Can we find a project with the given title?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.

        #print project

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        #positions = Position.objects.filter(project=project)

        # Adds our results list to the template context under title pages.
        #context_dict['positions'] = positions
        # We also add the project object from the database to the context dictionary.
        # We'll use this in the template to verify that the project exists.
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

            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'matching_system_project/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)