from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Project, Position, Application
from django.db import models

from django.forms import CharField
from django.core import validators

from forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate

from forms import ProjectForm, PositionForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from models import Application
from django.contrib.auth.models import User

from django.core.mail import send_mail, mail_admins
from django.core.mail.backends.smtp import EmailBackend
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def index(request):

    context = RequestContext(request )


    position_list = Position.objects.all()
    app_lisr=Application.objects.all()
    pos_list=[]
    ap_list=[]

    position_dict ={'positions':position_list,'applications':app_lisr}
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
       # profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            if User.objects.filter(email=user.email).exists():
               #  user_form.email.default_error_messages
                 print "error"
            else:
             user.set_password(user.password)
             user.save()
             registered = True
        else:
            print user_form.errors,
    else:
        user_form = UserForm()

    return render_to_response(
            'matching_system_project/register.html',
            {'user_form': user_form,  'registered': registered},
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

    print "he applied!!!!!"

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

def apply(request, uid, posid):


    # from django.core import mail
    #
    # connection = mail.get_connection()
    #
    # # email = EmailMessage('Hello', 'World', to=['davidb1985@gmail.com'])
    # connection.send_mail('Subject', 'Message.', 'from@example.com',
    #           ['john@example.com', 'jane@example.com'])
    #
    # connection.close()

    print "he applied!!!!!"


    pos = Position.objects.get(pk=posid)
    posuid = User.objects.get(pk=uid)

    print "position: " + pos.title + " applied for by: " + posuid.username

    existingApplications = len(Application.objects.filter(UserID = posuid, PositionID = pos))
    print existingApplications

    # print posuid
    # print pos.fk_ApplicantID

    if existingApplications < 1:

         Application.objects.create(
            UserID = posuid,
            PositionID = pos,
            accepted = False,
            seenByPM = False,)

    else:

         print "you cannot apply more than twice"



    # print user

    # feed=Feed.objects.get(pk=feedno)
    # t=request.META['REMOTE_ADDR']
    # feed.add_vote(t,+1)
    # vote, created = Vote.objects.get_or_create(
    #
    #     feed=feed,
    #     ip=t,
    #     )
    #
    # feed.likecount+=1
    # feed.save()
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect('/')





def accept(request,appid):

    app= Application.objects.get(pk=appid)

    if Application.objects.get(pk=appid).accepted == False:

        app.accepted = True
        app.seenByPM = True

        app.save()

        pos = Position.objects.get(pk=app.PositionID.id)
        pos.isOpen = False
        pos.fk_ApplicantID = app.UserID
        pos.save()

    #     send_mail( "Hellow", "Kak dela?",
    #     'matchingsystem.3sigma@yahoo.com',
    #     ['u.amrah@gmail.com'],
    #     auth_user='matchingsystem.3sigma',
    #     auth_password='Django2014', connection=EmailBackend(
    #         host='smtp.yahoo.com',
    #         port=587,
    #         username='matchingsystem.3sigma',
    #         password='Django2014',
    #         use_tls=True
    #     )
    # )


        send_mail("Test","Your text message! Data sent:  "  , 'matchingsystem.3sigma@yahoo.com',['u.amrah@gmail.com'], fail_silently=False )
        #mail_admins("other subject","some text",fail_silently=False)
       # Application.objects.set(seenByPm=True )
       # Application.objects.set(accepted=True )
     #  Application.objects.get(pk=appid).accepted=True
      # Application.objects.get(pk=appid).seenByPm=True
      # Application.objects.get(pk=appid).save()

        print Application.objects.get(pk=appid).PositionID
    else:
        print "cannot accept application more than once"

    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect('/')


def history(request):

     context = RequestContext(request)
     proj_list=Project.objects.all()
     pos_list=Position.objects.all()
     app_list =Application.objects.all()
     us_list=User.objects.all()
     context_dict={
     'projects':proj_list,
     'positions':pos_list,
     'applications':app_list,
                }


     return render_to_response('matching_system_project/history.html',context_dict,context)

