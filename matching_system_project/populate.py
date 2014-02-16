import os
import datetime
import time


def populate():

    add_project(name="Company Intranet",
                description="We are building a new intranet that brings mangement and development under one roof",
                created="2014-03-15",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True,)

    add_project(name="Fiberoptic infrastructure",
                description="New fiberoptics are important fot the future of the company, network engineers and architects are needed urgently for this overhaul.",
                created="2013-03-16",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True,)

    add_project(name="Information retrieval research group",
                description="The company is forming a group to research neural search. Lets build something awesome!",
                created="2013-03-16",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True,)

    add_project(name="Cow Milking Robot 3.0",
                description="The last cow milking robots were a huge disaster. University 2.0 must harness its bovine talent to suceed at this goal.",
                created="2013-03-16",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True,)

    add_project(name="Rector election app",
                description="Our students are lazy shits and don't vote enough for new Rectors. We are building a mobile app to get them involved.",
                created="2013-03-16",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True,)

    add_project(name="Automatic Will Smith detection device",
                description="Will Smith, formally known as the fresh price has been terrorizing campus students with awful films disguised as hollywood blockbusters. We need to manage this issue with a series of automatic turrets and will smith detection sensor arrays.",
                created="2013-03-16",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True,)

    add_project(name="Coffee dispensing website",
                description="I want a website that makes coffee for me. Don't tell me it isn't possible I've seen star trek.",
                created="2013-03-16",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True,)

def add_project(name, description, created, starts, expires, active):
    c = Project.objects.get_or_create(name=name, description=description, created=created, starts=starts, expires=expires, active=active)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_system_project.settings')
    from matching_system_project.models import Project
    populate()
