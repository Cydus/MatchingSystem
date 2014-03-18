from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    fk_CreatedBy = models.ForeignKey(User, null=True, blank=True)
    projectName = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=999)
    created = models.DateField(auto_now_add=True)
    starts = models.DateField(verbose_name="Start Date")
    expires = models.DateField(verbose_name="End Date")
    active = models.BooleanField(default=True)
    url = models.URLField(max_length=256)
    #
    # def save(self):
    #     if not self.url:
    #         self.url = "tttt"
    #     super(Project, self).save()
    #

    # def pre_save(self, request, extra_command="", *args, **kwargs):
    #     print "hihihihi"
    #     usr = request.user
    #     self.fk_CreatedBy = usr

    def post_save(self, request, extra_command="", *args, **kwargs):
        print "I HATE DJANGO"
        self.fk_CreatedBy = request.user
        self.save()

    def __unicode__(self):
        return self.projectName.lower()

class Position(models.Model):
    title = models.CharField(max_length=128)
    projectID = models.ForeignKey('Project')
    description = models.TextField(max_length=999)
    dateTimeCreated = models.DateField(auto_now_add=True)
    dateTimeStarts = models.DateField(verbose_name="Start Date")
    dateTimeExpires = models.DateField(verbose_name="End Date")
    url = models.URLField(max_length=256)

    fk_ApplicantID = models.ForeignKey(User, null=True, blank=True)
    isOpen = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title.lower()

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import signals

class Application(models.Model):
    UserID = models.ForeignKey(User)
    PositionID = models.ForeignKey(Position)
    dateTimeCreated = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    seenByPM = models.BooleanField(default=False)


    # url = models.CharField(max_length=128)
    # if (PositionID.isOpen == False):

    print "----------------- SETTING " + "" + " TO FALSE -------------------"

    # if Position.objects.get(title="Web Developer").isOpen:
    #     print "HALOOOOOOOOOOOOOOOOOOOOO"

    # print Position.objects.filter(title="Web Developer")
        # PositionID.isOpen = False

    # from django.core.signals import request_finished
    # import django.core.signals
    # # request_finished.connect(pre_save)

    def pre_save(self, extra_command="", *args, **kwargs):
        print "lol"
        print self.PositionID.title
        posID = self.PositionID._get_pk_val

        pos = Position.objects.get(pk=posID)
        print pos.isOpen

        pos.fk_ApplicantID = self.UserID
        pos.save()


        if (self.accepted == True):

            print "position has been accepted"

            pos.isOpen=False
            pos.save()

        # pos.save()

    def __unicode__(self):
        # + 'Project: ' + self.PositionID.ProjectID.projectName +

        print self.PositionID.title

        return (self.UserID.username + ' applied for: ' + self.PositionID.title)



def update_position(sender, instance, created, **kwargs):
    instance.pre_save()

    signals.post_save.connect(update_position, sender=Application)


def create_project(request, sender, instance, created, **kwargs):
    instance.post_save(request=request.user)


class UserProfile(models.Model):
    user = models.OneToOneField(User)


    # dob = models.DateField()

    # Override the __unicode__() method to return out something meaningful!

    def __unicode__(self):
        return self.user.username

# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)
#
#     # The additional attributes we wish to include.
#     website = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_images', blank=True)
#
#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username