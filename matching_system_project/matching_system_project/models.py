from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    # id automatically generated
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(name="End Date")
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Position(models.Model):
    # id automatically generated
    title = models.CharField(max_length=128)
    ApplicationID = models.ForeignKey('Project')
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(name="End Date")

    def __unicode__(self):
        return self.title

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
