from django import forms
from django.contrib.auth.models import User
from models import Project, Position, Application


class PositionForm(forms.ModelForm):
    # name = forms.CharField(max_length=128, help_text="Enter a position name")
    class Meta:
        model = Position

