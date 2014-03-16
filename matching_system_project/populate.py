import os
import datetime
import time


def populate():

    add_Group(name="Applicant")

    names = ["blushfold", "shyrope", "gearstall", "lightningsleepy", "napkingleaming", "vagueludicrous", "feathertangy", "stickersspare", "gonzobumper", "barerunny", "metalgoombah", "minergoldsword", "obtainablefalcon", "geldingprevious", "coatden", "lostpacked", "ticketslither", "dustercows", "bogglingbrain", "stupendousskirting", "rakingprofuse", "knobslipped", "noodlerubber", "shockunicyclist", "jawblobby", "snailtractor", "prettyunwieldy", "holytremendous", "windyflashing", "broadmeat", "rustleflippant", "sudaneseplaying", "snoopgolfing", "colonystormy", "brutaltooth", "quaintpelvis", "rollgeneration", "audiencefartlek", "ruddystinging", "lobsternippy", "itchgobbledygook", "glossyrook", "blizzardcheeks", "cluckhoitytoity", "apricottrap", "groverink", "leaptriathlete", "twitchyjohns", "rottenbutty", "spectaclesrare"]
    fnames = ["Mary", "Anna", "Emma", "Elizabeth", "Minnie", "Margaret", "Ida", "Alice", "Bertha", "Sarah", "Annie", "Clara", "Ella", "Florence", "Cora", "Martha", "Laura", "Nellie", "Grace", "Carrie", "Maude", "Mabel", "Bessie", "Jennie", "Gertrude", "Julia", "Hattie", "Edith", "Mattie", "Rose", "Catherine", "Lillian", "Ada", "Lillie", "Helen", "Jessie", "Louise", "Ethel", "Lula", "Myrtle", "Eva", "Frances", "Lena", "Lucy", "Edna", "Maggie", "Pearl", "Daisy", "Fannie", "Josephine"]
    lnames = ["Aaberg", "Aaron", "Abarca", "Abbate", "Abbess", "Abbott", "Abbratozzato", "Abdelnour", "Abderrazzaq", "Abdollah", "Abdous", "Abdullah", "Abdulrazak", "Abe", "Abel", "Abelmann", "Abelson", "Abernathy", "Abnet", "Abraham", "Abraham-Scalapino", "Abrams", "Abramson", "Abromson-Leeman", "Aburdene", "Acambages", "Accardo", "Accomazzi", "Achacoso", "Acker", "Ackerly", "Ackerman", "Acus", "Adair", "Adam", "Adame", "Adams", "Adamson", "Addison", "Ade", "Adelson", "Adelstein", "Adibe", "Adicho", "Adiele", "Adler", "Adolph", "Adorno", "Adourian", "Adrian-Haberly"]

    for i in range(len(names)):
        add_user(username=names[i],
            email=names[i]+"@gmail.com",
            firstname=fnames[i],
            lastname=lnames[i],
            password="password",
            is_staff=0
            )

    add_user(username="AJones49",
             email="davidb1985@gmail.com",
             firstname="Alexander",
             lastname="Jones",
             password="password",
             is_staff = 1,)

    add_user(username="Richard44",
             email="davidb1985@gmail.com",
             firstname="Richard",
             lastname="Anderson",
             password="password",
             is_staff = 0,)

    add_user(username="SarahJ",
             email="sarahjohnson@gmail.com",
             firstname="Sarah",
             lastname="Johnson",
             password="password",
             is_staff = 1,)

    add_user(username="SimonB",
             email="simon0124@gmail.com",
             firstname="Simon",
             lastname="Black",
             password="password",
             is_staff = 0,)

    add_user(username="Anne14",
             email="annebold@gmail.com",
             firstname="Anne",
             lastname="Bold",
             password="password",
             is_staff = 0,)

    add_user(username="Alex777",
             email="alex1802@gmail.com",
             firstname="Alexander",
             lastname="Powell",
             password="password",
             is_staff = 0,)

    add_user(username="Mike",
             email="mike@gmail.com",
             firstname="Michael",
             lastname="Barrows",
             password="password",
             is_staff=0, )



    intranet = add_project(projectName="Company Intranet",
                description="We are building a new intranet that brings management and development under one roof",
                created="2014-03-15",
                starts="2014-04-15",
                expires="2015-07-15",
                active=True,
                url="company_intranet",)

    infrastructure = add_project(projectName="Fibre optic infrastructure",
                description="New fiber optics are important for the future of the company, network engineers and architects are needed urgently for this overhaul.",
                created="2013-02-28",
                starts="2014-04-15",
                expires="2014-12-15",
                active=True,
                url="fibre_optic_infrastructure")

    informationRetrieval = add_project(projectName="Information Retrieval Research Group",
                description="The company is forming a group to research neural search. Let's build something awesome!",
                created="2014-03-02",
                starts="2014-03-25",
                expires="2014-08-15",
                active=True,
                url = "information_retrieval_research_group",)

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

    # Positions

    webDeveloper = add_position(title="Web Developer",
                 projectID=intranet,
                 description="Design web pages, sites or applications. Provide attractive and capable web applications",
                 dateTimeCreated="2014-03-20",
                 dateTimeStarts="2014-05-15",
                 dateTimeExpires="2015-02-10",
                 isOpen=True,
                 url="web_developer")

    informationArchitect = add_position(title="Information Architect",
                                projectID=intranet,
                                description="Develop the intranets navigation, menus and overall content structure. Applicant should be fully versed in information theroy and have a good idea of intranet usability",
                                dateTimeCreated="2014-03-20",
                                dateTimeStarts="2014-05-15",
                                dateTimeExpires="2015-02-10",
                                isOpen=True,
                                url="information-architect")


    networkArchitecture = add_position(title="Network Architect",
                 projectID=intranet,
                 description="Responsible for designing computer networks, including local area networks (LANs), wide area networks (WANs), the Internet, intranets, and other data communications systems. Creates, tests, and evaluates networks.",
                 dateTimeCreated="2014-03-22",
                 dateTimeStarts="2014-05-17",
                 dateTimeExpires="2015-02-01",
                 isOpen=True,
                 url="network_architect",)

    systemProgrammer = add_position(title="System Programmer",
                 projectID=infrastructure,
                 description="Produce, install and implement new and modified computer systems, networks and related operating software",
                 dateTimeCreated="2014-04-12",
                 dateTimeStarts="2014-05-25",
                 dateTimeExpires="2015-07-15",
                 isOpen=True,
                 url="system_programmer",)



    securitySpecialist = add_position(title="Security Specialist",
                 projectID=informationRetrieval,
                 description="Safeguards information system assets by identifying and solving potential and actual security problems.",
                 dateTimeCreated="2014-03-18",
                 dateTimeStarts="2014-05-01",
                 dateTimeExpires="2015-10-15",
                 isOpen=False,
                 url="security_specialist",)

    # Applications

    add_application(dateTimeCreated="2014-03-05",
                    accepted=False,
                    seenByPM=False,
                    UserID=User.objects.get(username='Mike'),
                    PositionID=webDeveloper,)


    add_application(dateTimeCreated="2014-03-08",
                    accepted=False,
                    seenByPM=True,
                    UserID=User.objects.get(username='AJones49'),
                    PositionID=securitySpecialist,)


    add_application(dateTimeCreated="2014-03-07",
                    accepted=True,
                    seenByPM=True,
                    UserID=User.objects.get(username='SarahJ'),
                    PositionID=networkArchitecture,)

    add_application(dateTimeCreated="2014-03-01",
                    accepted=True,
                    seenByPM=False,
                    UserID=User.objects.get(username='Anne14'),
                    PositionID=systemProgrammer,)


def add_project(projectName, description, created, starts, expires, active, url):
    c = Project.objects.get_or_create(url=url ,projectName=projectName, description=description, created=created, starts=starts, expires=expires, active=active)[0]
    return c

def add_Group(name):
    g = Group.objects.get_or_create(name=name)
    return g

def add_position(url, title, projectID, description, dateTimeCreated, dateTimeStarts, dateTimeExpires, isOpen):
    p = Position.objects.get_or_create(url=url, title=title, projectID=projectID, description=description, dateTimeCreated=dateTimeCreated,dateTimeStarts=dateTimeStarts, dateTimeExpires=dateTimeExpires, isOpen=isOpen)[0]
    return p

def add_user(username, email, firstname, lastname, password, is_staff):
    u = User.objects.get_or_create(username=username, email=email, first_name=firstname, last_name=lastname, password=password, is_staff = is_staff)
    return u

def add_application(UserID, PositionID, dateTimeCreated, accepted, seenByPM):
    a = Application.objects.get_or_create(dateTimeCreated=dateTimeCreated, accepted=accepted, seenByPM=seenByPM, UserID=UserID, PositionID=PositionID)
    return a


# Start execution here!
if __name__ == '__main__':
    print "Starting PMS population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_system_project.settings')
    from matching_system_project.models import Project, Position, Application

    from django.contrib.auth.models import Group, BaseUserManager, Permission, User, UserManager, AbstractUser, PermissionManager, PermissionsMixin, GroupManager
    populate()
