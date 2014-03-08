from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Project
from models import Position

from django.http import HttpResponse

def index(request):

    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    #context_dict = {'boldmessage': "I am bold font from the context"}
   # project_list = Project.objects.all()
  #  project_dict = {'projects': project_list}
    position_list = Position.objects.all()
    position_dict ={'positions':position_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
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

    print project_name

    project = Project.objects.get(projectName=project_name)

    # Change underscores in the project title to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the title.
    project_name = project_name_url.replace('_', ' ' )

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the title of the project passed by the user.
    context_dict = {'project_name': project_name}
    context_dict = {
        'boldmessage': project,
        'description': project.description,
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


