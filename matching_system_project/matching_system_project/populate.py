import os
import datetime

def populate():
    python_project = add_project('Python')

    add_project(project=python_project,
             title="Company Intranet",
             description="We are building a new intranet that brings mangement and development under one roof",
             created=datetime,
             starts=datetime,
             expires=datetime + datetime.timedelta(days=10),
             active=True)

    # add_page(project=python_project,
    #          title="How to Think like a Computer Scientist",
    #          url="http://www.greenteapress.com/thinkpython/")
    #
    # add_page(project=python_project,
    #          title="Learn Python in 10 Minutes",
    #          url="http://www.korokithakis.net/tutorials/python/")
    #
    # django_project = add_project("Django")
    #
    # add_page(project=django_project,
    #          title="Official Django Tutorial",
    #          url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    #
    # add_page(project=django_project,
    #          title="Django Rocks",
    #          url="http://www.djangorocks.com/")
    #
    # add_page(project=django_project,
    #          title="How to Tango with Django",
    #          url="http://www.tangowithdjango.com/")
    #
    # frame_project = add_project("Other Frameworks")
    #
    # add_page(project=frame_project,
    #          title="Bottle",
    #          url="http://bottlepy.org/docs/dev/")
    #
    # add_page(project=frame_project,
    #          title="Flask",
    #          url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Project.objects.all():
        for p in Page.objects.filter(project=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(project, title, url, views=0):
    p = Page.objects.get_or_create(project=project, title=title, url=url, views=views)[0]
    return p

def add_project(title):
    c = Project.objects.get_or_create(title=title)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from models import Project, Page
    populate()
