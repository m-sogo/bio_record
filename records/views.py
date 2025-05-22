#views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from .models import Species, Location, Record, Survey
from .forms import SpeciesForm, LocationForm, RecordForm, SurveyForm
from django.db.models import Q

#Home views
class HomeView(TemplateView):
    template_name = 'records/home.html'

# Survey views
class SurveyListView(ListView):
    model = Survey
    template_name = 'records/survey_list.html'
    context_object_name = 'surveys'

    def get_queryset(self):
        queryset = super().get_queryset()
        survey_query_y = self.request.GET.get('survey_y')
        survey_query_m = self.request.GET.get('survey_m')
        survey_query_d = self.request.GET.get('survey_d')

        if survey_query_y:
            queryset = queryset.filter(date__year=survey_query_y)
        if survey_query_m:
            queryset = queryset.filter(date__month=survey_query_m)
        if survey_query_d:
            queryset = queryset.filter(date__date=survey_query_d)

        queryset = queryset.order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['survey_query_y'] = self.request.GET.get('survey_y', '')
        context['survey_query_m'] = self.request.GET.get('survey_m', '')
        context['survey_query_d'] = self.request.GET.get('survey_d', '')
        return context

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
    context_object_name = 'survey'
    success_url = reverse_lazy('records:survey_list')

# Record views
class RecordListView(ListView):
    model = Record
    template_name = 'records/record_list.html'
    context_object_name = 'records'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        species_query = self.request.GET.get('species')
        location_query = self.request.GET.get('location')
        survey_query_y = self.request.GET.get('survey_y')
        survey_query_m = self.request.GET.get('survey_m')
        survey_query_d = self.request.GET.get('survey_d')
        survey_query_date = self.request.GET.get('survey_date')

        if species_query:
            queryset = queryset.filter(
                Q(species__name__icontains=species_query) |
                Q(species__genus__icontains=species_query) |
                Q(species__family__icontains=species_query) |
                Q(species__scientific_name__icontains=species_query)
            )
        if location_query:
            queryset = queryset.filter(location__name__icontains=location_query)
        if survey_query_y:
            queryset = queryset.filter(survey__date__year=survey_query_y)
        if survey_query_m:
            queryset = queryset.filter(survey__date__month=survey_query_m)
        if survey_query_d:
            queryset = queryset.filter(survey__date__day=survey_query_d)
        if survey_query_date:
            queryset = queryset.filter(survey__date=survey_query_date)
        
        queryset = queryset.order_by('-survey__date', 'location__name', 'species__name')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['species_query'] = self.request.GET.get('species', '')
        context['location_query'] = self.request.GET.get('location', '')
        context['survey_query_y'] = self.request.GET.get('survey_y', '')
        context['survey_query_m'] = self.request.GET.get('survey_m', '')
        context['survey_query_d'] = self.request.GET.get('survey_d', '')
        return context

class RecordDetailView(DetailView):
    model = Record
    template_name = 'records/record_detail.html'
    context_object_name = 'record'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['species'] = self.object.species
        context['location'] = self.object.location
        context['survey'] = self.object.survey
        return context

class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_create.html'
    success_url = reverse_lazy('records:record_list')

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
    success_url = reverse_lazy('records:record_list')

# Species views
class SpeciesListView(ListView):
    model = Species
    template_name = 'records/species_list.html'
    context_object_name = 'species'

    def get_queryset(self):
        queryset = super().get_queryset()
        name_query = self.request.GET.get('name')
        genus_query = self.request.GET.get('genus')
        family_query = self.request.GET.get('family')
        scientific_name_query = self.request.GET.get('scientific_name')

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)
        if genus_query:
            queryset = queryset.filter(genus__icontains=genus_query)
        if family_query:
            queryset = queryset.filter(family__icontains=family_query)
        if scientific_name_query:
            queryset = queryset.filter(scientific_name__icontains=scientific_name_query)

        queryset = queryset.order_by('family', 'genus')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_query'] = self.request.GET.get('name', '')
        context['genus_query'] = self.request.GET.get('genus', '')
        context['family_query'] = self.request.GET.get('family', '')
        context['scientific_name_query'] = self.request.GET.get('scientific_name', '')
        return context

class SpeciesDetailView(DetailView):
    model = Species
    template_name = 'records/species_detail.html'
    context_object_name = 'species'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['records'] = Record.objects.filter(species=self.object)
            return context

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

    def get_queryset(self):
        queryset = super().get_queryset()
        location_query = self.request.GET.get('location')

        if location_query:
            queryset = queryset.filter(name__icontains=location_query)

        queryset = queryset.order_by('name')
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['location_query'] = self.request.GET.get('location','')
        return context

class LocationDetailView(DetailView):
    model = Location
    template_name = 'records/location_detail.html'
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['records'] = Record.objects.filter(location=self.object).order_by('-survey__date')
            return context

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