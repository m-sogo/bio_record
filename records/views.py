#views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from .models import Species, Location, Record, Survey
from .forms import SpeciesForm, LocationForm, RecordForm, SurveyForm

#Home views
class HomeView(TemplateView):
    template_name = 'records/home.html'

# Survey views
class SurveyListView(ListView):
    model = Survey
    template_name = 'records/survey_list.html'
    context_object_name = 'surveys'

class SurveyDetailView(DetailView):
        model = Survey
        template_name = 'records/survey_detail.html'
        context_object_name = 'survey'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['records'] = Record.objects.filter(survey=self.object)
            return context

class SurveyCreateView(CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'records/survey_create.html'
    success_url = reverse_lazy('records:survey_list')
    
class SurveyUpdateView(UpdateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'records/survey_update.html'
    context_object_name = 'survey'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Survey, pk=pk)

    def get_success_url(self):
        return reverse_lazy('records:survey_detail', kwargs={'pk': self.object.pk})

class SurveyDeleteView(DeleteView):
    model = Survey
    template_name = 'records/survey_delete.html'
    context_object_name = 'record'
    success_url = reverse_lazy('records:survey_list')

# Record views
class RecordcompleteView(TemplateView):
    template_name = 'records/record_complete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        record = get_object_or_404(Record, pk=pk)
        context['record'] = record
        return context

class RecordDetailView(DetailView):
    model = Record
    template_name = 'records/record_detail.html'
    context_object_name = 'record'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = self.object.location
        context['survey'] = self.object.survey
        return context

class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_create.html'
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('records:record_complete', kwargs={'pk': self.object.pk})

class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_update.html'
    context_object_name = 'record'

    def get_success_url(self):
        return reverse_lazy('records:record_detail', kwargs={'pk': self.object.pk})

class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'records/record_delete.html'
    context_object_name = 'record'
    success_url = reverse_lazy('records:record_complete')

# Species views
class SpeciesListView(ListView):
    model = Species
    template_name = 'records/species_list.html'
    context_object_name = 'species'

class SpeciesDetailView(DetailView):
    model = Species
    template_name = 'records/species_detail.html'
    context_object_name = 'species'

class SpeciesCreateView(CreateView):
    model = Species
    form_class = SpeciesForm
    template_name = 'records/species_create.html'
    success_url = reverse_lazy('records:species_list')

class SpeciesUpdateView(UpdateView):
    model = Species
    form_class = SpeciesForm
    template_name = 'records/species_update.html'
    context_object_name = 'species'

    def get_success_url(self):
        return reverse_lazy('records:species_detail', kwargs={'pk': self.object.pk})

class SpeciesDeleteView(DeleteView):
    model = Species
    template_name = 'records/species_delete.html'
    context_object_name = 'species'
    success_url = reverse_lazy('records:species_list')

# Location views
class LocationListView(ListView):
    model = Location
    template_name = 'records/location_list.html'
    context_object_name = 'locations'

class LocationDetailView(DetailView):
    model = Location
    template_name = 'records/location_detail.html'
    context_object_name = 'location'

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'records/location_create.html'
    success_url = reverse_lazy('records:location_list')

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'records/location_update.html'
    context_object_name = 'location'

    def get_success_url(self):
        return reverse_lazy('records:location_detail', kwargs={'pk': self.object.pk})

class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'records/location_delete.html'
    context_object_name = 'location'
    success_url = reverse_lazy('records:location_list')