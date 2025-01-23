from django.urls import path
from . import views

urlpatterns = [
    # City Views
    path('cities/', views.CityListView.as_view(), name='city-list'),
    path('cities/new/', views.CityCreateView.as_view(), name='city-create'),
    path('cities/<int:pk>/', views.CityDetailView.as_view(), name='city-detail'),
    path('cities/<int:pk>/update/', views.CityUpdateView.as_view(), name='city-update'),
    path('cities/<int:pk>/delete/', views.CityDeleteView.as_view(), name='city-delete'),

    # Profession Views
    path('professions/', views.ProfessionListView.as_view(), name='profession-list'),
    path('professions/new/', views.ProfessionCreateView.as_view(), name='profession-create'),
    path('professions/<int:pk>/', views.ProfessionDetailView.as_view(), name='profession-detail'),
    path('professions/<int:pk>/update/', views.ProfessionUpdateView.as_view(), name='profession-update'),
    path('professions/<int:pk>/delete/', views.ProfessionDeleteView.as_view(), name='profession-delete'),

    # Sleep Duration Views
    path('sleep-durations/', views.SleepDurationListView.as_view(), name='sleep-duration-list'),
    path('sleep-durations/new/', views.SleepDurationCreateView.as_view(), name='sleep-duration-create'),
    path('sleep-durations/<int:pk>/', views.SleepDurationDetailView.as_view(), name='sleep-duration-detail'),
    path('sleep-durations/<int:pk>/update/', views.SleepDurationUpdateView.as_view(), name='sleep-duration-update'),
    path('sleep-durations/<int:pk>/delete/', views.SleepDurationDeleteView.as_view(), name='sleep-duration-delete'),

    # Dietary Habits Views
    path('dietary-habits/', views.DietaryHabitsListView.as_view(), name='dietary-habits-list'),
    path('dietary-habits/new/', views.DietaryHabitsCreateView.as_view(), name='dietary-habits-create'),
    path('dietary-habits/<int:pk>/', views.DietaryHabitsDetailView.as_view(), name='dietary-habits-detail'),
    path('dietary-habits/<int:pk>/update/', views.DietaryHabitsUpdateView.as_view(), name='dietary-habits-update'),
    path('dietary-habits/<int:pk>/delete/', views.DietaryHabitsDeleteView.as_view(), name='dietary-habits-delete'),

    # Degree Views
    path('degrees/', views.DegreeListView.as_view(), name='degree-list'),
    path('degrees/new/', views.DegreeCreateView.as_view(), name='degree-create'),
    path('degrees/<int:pk>/', views.DegreeDetailView.as_view(), name='degree-detail'),
    path('degrees/<int:pk>/update/', views.DegreeUpdateView.as_view(), name='degree-update'),
    path('degrees/<int:pk>/delete/', views.DegreeDeleteView.as_view(), name='degree-delete'),

    # Student Views
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/new/', views.StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
]
