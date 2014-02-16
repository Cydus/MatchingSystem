from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    # id automatically generated
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(verbose_name="End Date")
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class Position(models.Model):
    # id automatically generated
    title = models.CharField(max_length=128)
    ProjectID = models.ForeignKey('Project')
    # @TODO Update ER Diagram, winningAppID fk removed
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(name="End Date")

    def __unicode__(self):
        return self.title

class Offer(models.Model):
    # id automatically generated
    UserID = models.ForeignKey(User)
    ApplicationID = models.ForeignKey('Application')
    message = models.TextField(max_length=999)
    Accepted = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    expires = models.DateField(name="End Date")

    def __unicode__(self):
        return self.pk

class Application(models.Model):
    # id automatically generated
    UserID = models.ForeignKey(User)
    PositionID = models.ForeignKey('Position')
    message = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    expires = models.DateField(name="End Date")
    successful = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)

    def __unicode__(self):
        return (self.UserID.username + ' -> ' + '[' + self.PositionID.ProjectID.name + ']' + self.PositionID.name)
