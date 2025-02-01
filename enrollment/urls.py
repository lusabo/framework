from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [

    path('', lambda request: redirect('login')),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('home/', views.HomeView.as_view(), name='home'),

    # City Views
    path('cities/', views.CityListView.as_view(), name='city-list'),
    path('cities/new/', views.CityCreateView.as_view(), name='city-create'),
    path('cities/<int:pk>/', views.CityDetailView.as_view(), name='city-detail'),
    path('cities/<int:pk>/update/', views.CityUpdateView.as_view(), name='city-update'),
    path('cities/<int:pk>/delete/', views.CityDeleteView.as_view(), name='city-delete'),

    # Student Views
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/new/', views.StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    path('evaluation-metrics/', views.EvaluationMetricsView.as_view(), name='evaluation_metrics'),

]
