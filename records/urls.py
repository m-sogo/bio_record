#urls.py
from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('survey_list/', views.SurveyListView.as_view(), name='survey_list'),
    path('survey_create/', views.SurveyCreateView.as_view(), name='survey_create'),
    path('survey_detail/<int:pk>/', views.SurveyDetailView.as_view(), name='survey_detail'),
    path('survey_update/<int:pk>/', views.SurveyUpdateView.as_view(), name='survey_update'),
    path('survey_delete/<int:pk>/', views.SurveyDeleteView.as_view(), name='survey_delete'),
    path('record_complete/', views.RecordcompleteView.as_view(), name='record_complete'),
    path('record_create/', views.RecordCreateView.as_view(), name='record_create'),
    path('record_detail/<int:pk>/', views.RecordDetailView.as_view(), name='record_detail'),
    path('record_update/<int:pk>/', views.RecordUpdateView.as_view(), name='record_update'),
    path('record_delete/<int:pk>/', views.RecordDeleteView.as_view(), name='record_delete'),
    path('species_list/', views.SpeciesListView.as_view(), name='species_list'),
    path('species_create/', views.SpeciesCreateView.as_view(), name='species_create'),
    path('species_detail/<int:pk>/', views.SpeciesDetailView.as_view(), name='species_detail'),
    path('species_update/<int:pk>/', views.SpeciesUpdateView.as_view(), name='species_update'),
    path('species_delete/<int:pk>/', views.SpeciesDeleteView.as_view(), name='species_delete'),
    path('location_list/', views.LocationListView.as_view(), name='location_list'),
    path('location_create/', views.LocationCreateView.as_view(), name='location_create'),
    path('location_detail/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('location_update/<int:pk>/', views.LocationUpdateView.as_view(), name='location_update'),
    path('location_delete/<int:pk>/', views.LocationDeleteView.as_view(), name='location_delete'),
]