import re

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Library
from django.template.defaultfilters import stringfilter

from models import Project, Position
from forms import UserForm
from forms import ProjectForm, PositionForm
from models import Application


register = Library()


def paragraphs(value):
    paras = re.split(r'[\r\n]+', value)
    paras = ['<p>%s</p>' % p.strip() for p in paras]
    return '\n'.join(paras)


paragraphs = stringfilter(paragraphs)

register.filter(paragraphs)


def index(request):
    context = RequestContext(request)

    position_list = Position.objects.all()
    app_list = Application.objects.all()
    pos_list = []
    ap_list = []
    for p in position_list:
        p.description = paragraphs(p.description)
        pos_list.append(p)

    position_dict = {'positions': pos_list, 'applications': app_list}
    return render_to_response('matching_system_project/index.html',
                              position_dict, context)

def projects(request):
    return HttpResponse("PROJECTS IN YOUR FACE MOFO")


def project(request, project_name_url):
    context = RequestContext(request)
    project_name = project_name_url.replace('_', ' ')

    project = Project.objects.get(url=project_name_url)

    project_name = project_name_url.replace('_', ' ')
    app_list = Application.objects.all()

    position_list = Position.objects.all()
    print position_list
    p_list = []
    for p in position_list:
        p.description = paragraphs(p.description)
        p_list.append(p)

    position_dict = {'positions': position_list}

    context_dict = {'project_name': project_name}
    context_dict = {
        'projectName': project.projectName,
        'description': project.description,
        'position_list': p_list,
        'applications': app_list,

    }

    try:

        context_dict['project'] = project
    except Project.DoesNotExist:
        # We get here if we didn't find the specified project.
        # Don't do anything - the template displays the "no project" message for us.
        pass

    # return HttpResponse("I AM A PROJECT")
    return render_to_response('matching_system_project/project.html',
                              context_dict, context)


def add_project(request):
    context = RequestContext(request)
    if request.method == 'POST':

        form = ProjectForm(request.POST)
        if form.is_valid():

            form.save(commit=True)
            return add_position(request)
        else:
            print form.errors
    else:

        nn = request.META.__getitem__("USER")
        print request
        form = ProjectForm(
            {'fk_CreatedBy': User.objects.get(username=request.user.username)})

    return render_to_response('matching_system_project/add_project.html',
                              {'form': form}, context)


def add_position(request):
    print request

    context = RequestContext(request)

    if request.method == 'POST':

        try:
            reqProject = request.POST.__getitem__("projectName")
            reqStarts = request.POST.__getitem__("starts")
            reqExpires = request.POST.__getitem__("expires")

            import forms

            context["projectName"] = reqProject
            form = PositionForm(
                {'projectID': reqProject, "dateTimeStarts": reqStarts,
                 "dateTimeExpires": reqExpires})

        except:

            import forms

            form = PositionForm(request.POST)

        if form.is_valid():

            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:

        form = PositionForm()

    return render_to_response('matching_system_project/add_position.html',
                              {'form': form}, context)


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            user.set_password((user.password))
            user.save()
            registered = True

            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)

        else:
            print user_form.errors,

    else:
        user_form = UserForm()

    return render_to_response(
        'matching_system_project/register.html',
        {'user_form': user_form, 'registered': registered},
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
        return render_to_response('matching_system_project/login.html', {},
                                  context)


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def applist(request):
    print "he applied!!!!!"

    context = RequestContext(request)
    proj_list = Project.objects.all()
    pos_list = Position.objects.all()
    app_list = Application.objects.all()
    us_list = User.objects.all()

    context_dict = {
        'projects': proj_list,
        'positions': pos_list,
        'applications': app_list,
        # 'users':us_list,
    }
    return render_to_response('matching_system_project/applist.html',
                              context_dict, context)


def pmprojects(request):
    print "he applied!!!!!"

    context = RequestContext(request)
    proj_list = Project.objects.all()
    pos_list = Position.objects.all()
    app_list = Application.objects.all()
    us_list = User.objects.all()

    context_dict = {
        'projects': proj_list,
        'positions': pos_list,
        'applications': app_list,
        'user': request.user,
    }
    return render_to_response('matching_system_project/pm-projects.html',
                              context_dict, context)


def apply(request, uid, posid):
    print "he applied!!!!!"

    pos = Position.objects.get(pk=posid)
    posuid = User.objects.get(pk=uid)

    print "position: " + pos.title + " applied for by: " + posuid.username

    existingApplications = len(
        Application.objects.filter(UserID=posuid, PositionID=pos))
    print existingApplications

    if existingApplications < 1:

        Application.objects.create(
            UserID=posuid,
            PositionID=pos,
            accepted=False,
            seenByPM=False, )

    else:

        print "you cannot apply more than twice"

    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect('/')


def accept(request, appid):
    if request.user.is_authenticated:
        app = Application.objects.get(pk=appid)

        if Application.objects.get(pk=appid).accepted == False:

            app.accepted = True
            app.seenByPM = True

            app.save()

            pos = Position.objects.get(pk=app.PositionID.id)
            pos.isOpen = False
            pos.fk_ApplicantID = app.UserID
            pos.save()

            embod = "Dear, " + app.UserID.first_name + " " + app.UserID.last_name + ",your application  for a   " + pos.title + " position " + " in " + pos.projectID.projectName + " was successfull." \
                    + " Regards,  " + pos.projectID.fk_CreatedBy.first_name + "  " + pos.projectID.fk_CreatedBy.last_name

            send_mail("Project Matching System", embod, 'vaspetr506@gmail.com',
                      [pos.fk_ApplicantID.email], fail_silently=False)

            print Application.objects.get(pk=appid).PositionID
        else:
            print "cannot accept application more than once"

        if 'HTTP_REFERER' in request.META:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return HttpResponseRedirect('/')


def history(request):
    context = RequestContext(request)
    proj_list = Project.objects.all()
    pos_list = Position.objects.all()
    app_list = Application.objects.all()
    us_list = User.objects.all()
    context_dict = {
        'projects': proj_list,
        'positions': pos_list,
        'applications': app_list,
    }

    return render_to_response('matching_system_project/history.html',
                              context_dict, context)

