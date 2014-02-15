import os
import datetime
import time


def populate():

    add_project(title="Company Intranet",
                description="We are building a new intranet that brings mangement and development under one roof",
                created="2014-03-15",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True)

    add_project(title="Company Intranet",
                description="We are building a new intranet that brings mangement and development under one roof",
                created="2014-03-15",
                starts="2014-03-15",
                expires="2014-03-15",
                active=True)

def add_project(title, description, created, starts, expires, active):
    c = Project.objects.get_or_create(title=title, description=description, created=created, starts=starts, expires=expires, active=active)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_system_project.settings')
    from matching_system_project.models import Project
    populate()
