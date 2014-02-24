import os
import datetime
import time


def populate():

    add_Group(name="Project Manager")
    add_Group(name="Applicant")
    add_Group(name="assholes")

    intranet = add_project(projectName="Company Intranet",
                description="We are building a new intranet that brings management and development under one roof",
                created="2014-03-15",
                starts="2014-04-15",
                expires="2015-07-15",
                active=True,)

    from matching_system_project.models import Project

    add_position(title="Web Developer",
                 projectID=intranet,
                 description="ff",
                 dateTimeCreated="2014-03-20",
                 dateTimeStarts="2014-05-15",
                 dateTimeExpires="2015-02-10",
                 isOpen=True,)

    # add_application(dateTimeCreated="2014-03-23",
    #                 accepted=False,
    #                 seenByPM=False,)





    # add_user(username="Mike",
    #          password="football",
    #          emailAddress="mike@gmail.com",
    #          firstName="Michael",
    #          surname="Barrows",)
    #
    # add_userProfile(user="Mike",
    #                 interest="java",)

    # add_project(name="Fiber optic infrastructure",
    #             description="New fiber optics are important fot the future of the company, network engineers and architects are needed urgently for this overhaul.",
    #             created="2013-03-16",
    #             starts="2014-04-15",
    #             expires="2014-12-15",
    #             active=True,)
#
#     add_project(name="Information retrieval research group",
#                 description="The company is forming a group to research neural search. Lets build something awesome!",
#                 created="2014-03-16",
#                 starts="2014-04-15",
#                 expires="2014-08-15",
#                 active=True,)
#
#     add_project(name="Cow Milking Robot 3.0",
#                 description="The last cow milking robots were a huge disaster. University 2.0 must harness its bovine talent to suceed at this goal.",
#                 created="2014-03-23",
#                 starts="2014-05-15",
#                 expires="2014-09-15",
#                 active=True,)
#
#     add_project(name="Rector election app",
#                 description="Our students are lazy shits and don't vote enough for new Rectors. We are building a mobile app to get them involved.",
#                 created="2014-03-25",
#                 starts="2014-04-28",
#                 expires="2014-08-19",
#                 active=True,)
#
#     add_project(name="Automatic Will Smith detection device",
#                 description="Will Smith, formally known as the fresh price has been terrorizing campus students with awful films disguised as hollywood blockbusters. We need to manage this issue with a series of automatic turrets and will smith detection sensor arrays.",
#                 created="2014-03-26",
#                 starts="2014-04-25",
#                 expires="2014-11-25",
#                 active=True,)
#
#     add_project(name="Coffee dispensing website",
#                 description="I want a website that makes coffee for me. Don't tell me it isn't possible I've seen star trek.",
#                 created="2014-04-26",
#                 starts="2014-05-18",
#                 expires="2014-0-25",
#                 active=True,)

def add_project(projectName, description, created, starts, expires, active):
    c = Project.objects.get_or_create(projectName=projectName, description=description, created=created, starts=starts, expires=expires, active=active)[0]
    return c

def add_Group(name):
    g = Group.objects.get_or_create(name=name)
    return g

def add_position(title, projectID, description, dateTimeCreated, dateTimeStarts, dateTimeExpires, isOpen):
    p = Position.objects.get_or_create(title=title, projectID=projectID, description=description, dateTimeCreated=dateTimeCreated,dateTimeStarts=dateTimeStarts, dateTimeExpires=dateTimeExpires, isOpen=isOpen)[0]
    return p

def add_application(dateTimeCreated, accepted, seenByPM):
    a = Application.objects.get_or_create(dateTimeCreated=dateTimeCreated, accepted=accepted, seenByPM=seenByPM)
    return a

# def add_user():
#     u = User.objects.get_or_create()
#     return u
#
# def add_userProfile(user, interest):
#     u = UserProfile(user=user, interest=interest)
#     return u


# Start execution here!
if __name__ == '__main__':
    print "Starting PMS population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_system_project.settings')
    from matching_system_project.models import Project, Position, Application
        #, UserProfile, User
    from django.contrib.auth.models import Group, Permission
    populate()
