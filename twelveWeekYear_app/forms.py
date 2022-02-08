from tkinter import Widget
from django import forms
from .models import *


class TwelveWeekForm(forms.ModelForm):
    class Meta:
        model = TwelveWeek
        fields = ["title", "start_date"]

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["title", "TwelveWeek", "due_date", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={ "placeholder": "Type your goal here..."}),
            "due_date": forms.DateInput(),
            "tags": forms.Select()
        }


class TacticForm(forms.ModelForm):
    class Meta:
        model = Tactic
        fields = ["title", "goal","start_date", "end_date", "frequency", "status"]
        # widgets = {
        #     "title": forms.TextInput(attrs={"placeholder": "Type your goal here..."}),
        #     "due_date": forms.DateInput(),
        #     "tags": forms.Select()
        # }
