from django.contrib.auth.models import User

from django import forms

from models import Project, Position
from models import UserProfile

dateTimeCreated = forms.TextInput(attrs={'size': 10, 'title': 'Your name', })


class ProjectForm(forms.ModelForm):
    projectName = forms.CharField(max_length=128,
                                  help_text="Enter a project name")
    description = forms.CharField(max_length=999,
                                  help_text="Describe the project")
    starts = forms.DateField(
        help_text="When will the project start? (dd/mm/YYYY)")
    expires = forms.DateField(
        help_text="When will the project end? (dd/mm/YYYY)")
    url = forms.CharField(max_length=256, help_text="Enter the URL")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Project


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
    projectID = forms.ModelChoiceField(queryset=Project.objects.all(),
                                       help_text="Select Project")
    description = forms.CharField(max_length=999,
                                  help_text="Describe the position")

    dateTimeStarts = forms.DateField(
        help_text="Enter the date when the position will start")
    dateTimeExpires = forms.DateField(
        help_text="Enter the date when the position will expire")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Position


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
                               help_text="Please enter a password.")
    email = forms.CharField(help_text="Please enter your email.",
                            error_messages={
                                'invalid': 'User with this e-mail already registred'})
    username = forms.CharField(help_text="Please enter a username.")
    first_name = forms.CharField(help_text="Enter your first name.")
    last_name = forms.CharField(help_text="Enter your last name")
    is_staff = 0


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

