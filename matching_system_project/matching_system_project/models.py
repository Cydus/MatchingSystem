from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    fk_CreatedBy = models.ForeignKey(User, null=False, blank=False, editable=True, auto_created=User)
    projectName = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(verbose_name="End Date")
    active = models.BooleanField(default=True, editable=False)
    url = models.CharField(max_length=256)

    def post_save(self, request, extra_command="", *args, **kwargs):
        print "I LIKE DJANGO"
        self.fk_CreatedBy = request.user
        self.save()

    def __unicode__(self):
        return self.projectName.lower()

class Position(models.Model):
    title = models.CharField(max_length=128)
    projectID = models.ForeignKey('Project')
    description = models.TextField(max_length=999)
    dateTimeCreated = models.DateField(auto_now_add=True, editable=False)
    dateTimeStarts = models.DateField(verbose_name="Start Date")
    dateTimeExpires = models.DateField(verbose_name="End Date")
    url = models.CharField(max_length=256, editable=False)

    fk_ApplicantID = models.ForeignKey(User, null=True, blank=True, editable=False)
    isOpen = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return self.title.lower()

# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver

from django.db.models import signals

class Application(models.Model):
    UserID = models.ForeignKey(User)
    PositionID = models.ForeignKey(Position)
    dateTimeCreated = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    seenByPM = models.BooleanField(default=False)


    print "------ SETTING " + "" + " TO FALSE ---------"

    def pre_save(self, extra_command="", *args, **kwargs):
        print "lol"
        print self.PositionID.title
        posID = self.PositionID._get_pk_val

        pos = Position.objects.get(pk=posID)
        print pos.isOpen

        pos.fk_ApplicantID = self.UserID
        print "WWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        pos.save()


        if (self.accepted == True):

            print "position has been accepted"

            pos.isOpen=False
            pos.save()


    def __unicode__(self):

        print self.PositionID.title

        return (self.UserID.username + ' applied for: ' + self.PositionID.title)



def update_position(sender, instance, created, **kwargs):
    instance.post_save()

    signals.post_save.connect(update_position, sender=Application)


def create_project(request, sender, instance, created, **kwargs):
    instance.post_save(request=request.user)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username
