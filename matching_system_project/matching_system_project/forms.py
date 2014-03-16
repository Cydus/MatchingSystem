from django import forms
from django.contrib.auth.models import User
from models import Project, Position, Application


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

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Project

        fields = ('projectName', 'description', 'created', 'starts', 'expires', 'active', 'url')



class PositionForm(forms.ModelForm):

    from models import Project

    title = forms.CharField(max_length=128, help_text="Enter a position name")
    projectID = forms.ModelChoiceField(queryset=Project.objects.all())
    # projectID = forms.ModelChoiceField(Project.objects.all(p))
    description = forms.CharField(max_length=999, help_text="Describe the position")
    dateTimeCreated = forms.DateField(help_text="Enter the date when the position was created")
    dateTimeStarts = forms.DateField(help_text="Enter the date when the position will start")
    dateTimeExpires = forms.DateField(help_text="Enter the date when the position will expire")
    url = forms.URLField(max_length=256, help_text="Enter the URL")
    isOpen = forms.BooleanField(help_text="Tick the box if the position is open")


    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Position
        # fields = ('title', 'description', 'dateTimeCreated', 'dateTimeStarts', 'dateTimeExpires', 'url', 'isOpen')






# class ApplicationForm(forms.ModelForm):
#     dateTimeCreated = forms.DateField()
#     accepted = forms.BooleanField()
#     seenByPM = forms.BooleanField()
#
#     class Meta:
#         model = Application


