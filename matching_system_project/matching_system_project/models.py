from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    projectName = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(verbose_name="End Date")
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.projectName

class Position(models.Model):
    title = models.CharField(max_length=128)
    projectID = models.ForeignKey('Project')
    description = models.TextField(max_length=999)
    dateTimeCreated = models.DateField(auto_now_add=True)
    dateTimeStarts = models.DateField(verbose_name="Start Date")
    dateTimeExpires = models.DateField(verbose_name="End Date")

    fk_ApplicantID = models.ForeignKey(User, null=True, blank=True)
    isOpen = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Application(models.Model):
    UserID = models.ForeignKey(User)
    PositionID = models.ForeignKey(Position)
    dateTimeCreated = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    seenByPM = models.BooleanField(default=False)

    def __unicode__(self):
        # + 'Project: ' + self.PositionID.ProjectID.projectName +
        return (self.UserID.username + ' applied for: ' + self.PositionID.title)

