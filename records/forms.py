#forms.py
from django import forms
from .models import Species,Location, Record, Survey
from django.utils import timezone

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ('name','genus','family','scientific_name')

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name','latitude','longitude','note')

class SurveyForm(forms.ModelForm):
    date = forms.DateField(initial=timezone.now().date())
    class Meta:
        model = Survey
        fields = ('date','note')

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('species','location','survey','count','length','weight','water_temperature','flow_rate','water_depth','note')
