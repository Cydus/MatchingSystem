from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    # id automatically generated
    projectName = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(verbose_name="End Date")
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.projectName

class Position(models.Model):
    # id automatically generated
    title = models.CharField(max_length=128)
    ProjectID = models.ForeignKey('Project')
    # @TODO Update ER Diagram, winningAppID fk removed
    description = models.TextField(max_length=999)
    dateTimeCreated = models.DateField(auto_now_add=True)
    dateTimeStarts = models.DateField(verbose_name="Start Date")
    dateTimeExpires = models.DateField(name="End Date")

    fk_ApplicantID = models.ForeignKey(User, null=True, blank=True)
    #fk_MProjectManager = models.ForeignKey(default=User.email)
    isOpen = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Application(models.Model):
    # id automatically generated
    UserID = models.ForeignKey(User)
    PositionID = models.ForeignKey('Position')
    dateTimeCreated = models.DateField(auto_now_add=True)
    #expires = models.DateField(name="End Date")
    accepted = models.BooleanField(default=False)
    seenByPM = models.BooleanField(default=False)

    def __unicode__(self):
        return (self.UserID.username + ' applied for:  ' + 'Project: ' + self.PositionID.ProjectID.projectName + ' |  Position: ' + self.PositionID.title)
