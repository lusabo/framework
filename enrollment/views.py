from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .models import City, Profession, SleepDuration, DietaryHabits, Degree, Student
from .forms import StudentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

# City Views
class CityListView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'city/list.html'
    context_object_name = 'cities'

class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    fields = ['name']
    template_name = 'city/form.html'
    success_url = reverse_lazy('city-list')

class CityDetailView(LoginRequiredMixin, DetailView):
    model = City
    template_name = 'city/details.html'
    context_object_name = 'city'

class CityUpdateView(LoginRequiredMixin, UpdateView):
    model = City
    fields = ['name']
    template_name = 'city/form.html'
    success_url = reverse_lazy('city-list')

class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'city/confirm_delete.html'
    success_url = reverse_lazy('city-list')

# Profession Views
class ProfessionListView(LoginRequiredMixin, ListView):
    model = Profession
    template_name = 'profession/list.html'
    context_object_name = 'professions'

class ProfessionCreateView(LoginRequiredMixin, CreateView):
    model = Profession
    fields = ['name']
    template_name = 'profession/form.html'
    success_url = reverse_lazy('profession-list')

class ProfessionDetailView(LoginRequiredMixin, DetailView):
    model = Profession
    template_name = 'profession/detail.html'
    context_object_name = 'profession'

class ProfessionUpdateView(LoginRequiredMixin, UpdateView):
    model = Profession
    fields = ['name']
    template_name = 'profession/form.html'
    success_url = reverse_lazy('profession-list')

class ProfessionDeleteView(LoginRequiredMixin, DeleteView):
    model = Profession
    template_name = 'profession/confirm_delete.html'
    success_url = reverse_lazy('profession-list')

# Sleep Duration Views
class SleepDurationListView(LoginRequiredMixin, ListView):
    model = SleepDuration
    template_name = 'sleepduration/list.html'
    context_object_name = 'sleep_durations'

class SleepDurationCreateView(LoginRequiredMixin, CreateView):
    model = SleepDuration
    fields = ['name']
    template_name = 'sleepduration/form.html'
    success_url = reverse_lazy('sleep-duration-list')

class SleepDurationDetailView(LoginRequiredMixin, DetailView):
    model = SleepDuration
    template_name = 'sleepduration/detail.html'
    context_object_name = 'sleep_duration'

class SleepDurationUpdateView(LoginRequiredMixin, UpdateView):
    model = SleepDuration
    fields = ['name']
    template_name = 'sleepduration/form.html'
    success_url = reverse_lazy('sleep-duration-list')

class SleepDurationDeleteView(LoginRequiredMixin, DeleteView):
    model = SleepDuration
    template_name = 'sleepduration/confirm_delete.html'
    success_url = reverse_lazy('sleep-duration-list')

# Dietary Habits Views
class DietaryHabitsListView(LoginRequiredMixin, ListView):
    model = DietaryHabits
    template_name = 'dietaryhabits/list.html'
    context_object_name = 'dietary_habits'

class DietaryHabitsCreateView(LoginRequiredMixin, CreateView):
    model = DietaryHabits
    fields = ['name']
    template_name = 'dietaryhabits/form.html'
    success_url = reverse_lazy('dietary-habits-list')

class DietaryHabitsDetailView(LoginRequiredMixin, DetailView):
    model = DietaryHabits
    template_name = 'dietaryhabits/detail.html'
    context_object_name = 'dietary_habit'

class DietaryHabitsUpdateView(LoginRequiredMixin, UpdateView):
    model = DietaryHabits
    fields = ['name']
    template_name = 'dietaryhabits/form.html'
    success_url = reverse_lazy('dietary-habits-list')

class DietaryHabitsDeleteView(LoginRequiredMixin, DeleteView):
    model = DietaryHabits
    template_name = 'dietaryhabits/confirm_delete.html'
    success_url = reverse_lazy('dietary-habits-list')

# Degree Views
class DegreeListView(LoginRequiredMixin, ListView):
    model = Degree
    template_name = 'degree/list.html'
    context_object_name = 'degrees'

class DegreeCreateView(LoginRequiredMixin, CreateView):
    model = Degree
    fields = ['name']
    template_name = 'degree/form.html'
    success_url = reverse_lazy('degree-list')

class DegreeDetailView(LoginRequiredMixin, DetailView):
    model = Degree
    template_name = 'degree/detail.html'
    context_object_name = 'degree'

class DegreeUpdateView(LoginRequiredMixin, UpdateView):
    model = Degree
    fields = ['name']
    template_name = 'degree/form.html'
    success_url = reverse_lazy('degree-list')

class DegreeDeleteView(LoginRequiredMixin, DeleteView):
    model = Degree
    template_name = 'degree/confirm_delete.html'
    success_url = reverse_lazy('degree-list')

# Student Views
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/form.html'
    success_url = reverse_lazy('student-list')

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['name', 'date_birth', 'gender', 'city', 'profession', 'academic_pressure', 'work_pressure', 'cgpa',
              'study_satisfaction', 'job_satisfaction', 'sleep_duration', 'dietary_habits', 'degree',
              'suicidal_thoughts', 'work_study_hour', 'financial_stress', 'family_history_mental_illness']
    template_name = 'student/form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/confirm_delete.html'
    success_url = reverse_lazy('student-list')
