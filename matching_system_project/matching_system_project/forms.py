from django import forms
from django.contrib.auth.models import User
from models import Project, Position, Application

from matching_system_project.models import UserProfile
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
    projectName = forms.CharField(max_length=128, help_text="Enter a project name")
    description = forms.CharField(max_length=999, help_text="Describe the project")
    created = forms.DateField(help_text="Enter the date for creating this project")
    starts = forms.DateField(help_text="Enter the start day for the project")
    expires = forms.DateField(help_text="Enter the expiration date")
    active = forms.BooleanField(help_text="Is this project active yet?")
    url = forms.URLField(max_length=256, help_text="Enter the URL")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Project

        fields = ('projectName', 'description', 'created', 'starts', 'expires', 'active', 'url')

def __init__(self, *args, **kwargs):
            self._user = kwargs.pop('user')
            # self._user = kwargs.pop()
            super(ProjectForm, self).__init__(*args, **kwargs)

def save(self, commit=True):
            inst = super(ProjectForm, self).save(commit=False)
            inst.fk_CreatedBy = self._user
            if commit:
                inst.save()
                self.save_m2m()
            return inst



class PositionForm(forms.ModelForm):

    from models import Project

    title = forms.CharField(max_length=128, help_text="Enter a position name")
    projectID = forms.ModelChoiceField(queryset=Project.objects.all())
    description = forms.CharField(max_length=999, help_text="Describe the position")
    dateTimeCreated = forms.DateField(help_text="Enter the date when the position was created")
    dateTimeStarts = forms.DateField(help_text="Enter the date when the position will start")
    dateTimeExpires = forms.DateField(help_text="Enter the date when the position will expire")
    url = forms.URLField(max_length=256, help_text="Enter the URL")
    isOpen = forms.BooleanField(help_text="Tick the box if the position is open")


    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Position

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name= forms.CharField
    last_name=forms.CharField
    is_staff=0
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):
     class Meta:
        model = UserProfile
        # fields = ('dob',)


