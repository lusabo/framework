from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import City, Profession, SleepDuration, DietaryHabits, Degree, Student
from django.urls import reverse_lazy

# City Views
class CityListView(ListView):
    model = City
    template_name = 'city/list.html'
    context_object_name = 'cities'

class CityCreateView(CreateView):
    model = City
    fields = ['name']
    template_name = 'city/form.html'
    success_url = reverse_lazy('city-list')

class CityDetailView(DetailView):
    model = City
    template_name = 'city_detail.html'
    context_object_name = 'city'

class CityUpdateView(UpdateView):
    model = City
    fields = ['name']
    template_name = 'city/form.html'
    success_url = reverse_lazy('city-list')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'city/confirm_delete.html'
    success_url = reverse_lazy('city-list')

# Profession Views
class ProfessionListView(ListView):
    model = Profession
    template_name = 'profession/list.html'
    context_object_name = 'professions'

class ProfessionCreateView(CreateView):
    model = Profession
    fields = ['name']
    template_name = 'profession/form.html'
    success_url = reverse_lazy('profession-list')

class ProfessionDetailView(DetailView):
    model = Profession
    template_name = 'profession/detail.html'
    context_object_name = 'profession'

class ProfessionUpdateView(UpdateView):
    model = Profession
    fields = ['name']
    template_name = 'profession/form.html'
    success_url = reverse_lazy('profession-list')

class ProfessionDeleteView(DeleteView):
    model = Profession
    template_name = 'profession/confirm_delete.html'
    success_url = reverse_lazy('profession-list')

# Sleep Duration Views
class SleepDurationListView(ListView):
    model = SleepDuration
    template_name = 'sleepduration/list.html'
    context_object_name = 'sleep_durations'

class SleepDurationCreateView(CreateView):
    model = SleepDuration
    fields = ['name']
    template_name = 'sleepduration/form.html'
    success_url = reverse_lazy('sleep-duration-list')

class SleepDurationDetailView(DetailView):
    model = SleepDuration
    template_name = 'sleepduration/detail.html'
    context_object_name = 'sleep_duration'

class SleepDurationUpdateView(UpdateView):
    model = SleepDuration
    fields = ['name']
    template_name = 'sleepduration/form.html'
    success_url = reverse_lazy('sleep-duration-list')

class SleepDurationDeleteView(DeleteView):
    model = SleepDuration
    template_name = 'sleepduration/confirm_delete.html'
    success_url = reverse_lazy('sleep-duration-list')

# Dietary Habits Views
class DietaryHabitsListView(ListView):
    model = DietaryHabits
    template_name = 'dietaryhabits/list.html'
    context_object_name = 'dietary_habits'

class DietaryHabitsCreateView(CreateView):
    model = DietaryHabits
    fields = ['name']
    template_name = 'dietaryhabits/form.html'
    success_url = reverse_lazy('dietary-habits-list')

class DietaryHabitsDetailView(DetailView):
    model = DietaryHabits
    template_name = 'dietaryhabits/detail.html'
    context_object_name = 'dietary_habit'

class DietaryHabitsUpdateView(UpdateView):
    model = DietaryHabits
    fields = ['name']
    template_name = 'dietaryhabits/form.html'
    success_url = reverse_lazy('dietary-habits-list')

class DietaryHabitsDeleteView(DeleteView):
    model = DietaryHabits
    template_name = 'dietaryhabits/confirm_delete.html'
    success_url = reverse_lazy('dietary-habits-list')

# Degree Views
class DegreeListView(ListView):
    model = Degree
    template_name = 'degree/list.html'
    context_object_name = 'degrees'

class DegreeCreateView(CreateView):
    model = Degree
    fields = ['name']
    template_name = 'degree/form.html'
    success_url = reverse_lazy('degree-list')

class DegreeDetailView(DetailView):
    model = Degree
    template_name = 'degree/detail.html'
    context_object_name = 'degree'

class DegreeUpdateView(UpdateView):
    model = Degree
    fields = ['name']
    template_name = 'degree/form.html'
    success_url = reverse_lazy('degree-list')

class DegreeDeleteView(DeleteView):
    model = Degree
    template_name = 'degree/confirm_delete.html'
    success_url = reverse_lazy('degree-list')

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'date_birth', 'gender', 'city', 'profession', 'academic_pressure', 'work_pressure', 'cgpa',
              'study_satisfaction', 'job_satisfaction', 'sleep_duration', 'dietary_habits', 'degree',
              'suicidal_thoughts', 'work_study_hour', 'financial_strees', 'family_history_mental_illness',
              'risk_of_drepession']
    template_name = 'student/form.html'
    success_url = reverse_lazy('student-list')

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'date_birth', 'gender', 'city', 'profession', 'academic_pressure', 'work_pressure', 'cgpa',
              'study_satisfaction', 'job_satisfaction', 'sleep_duration', 'dietary_habits', 'degree',
              'suicidal_thoughts', 'work_study_hour', 'financial_strees', 'family_history_mental_illness',
              'risk_of_drepession']
    template_name = 'student/form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/confirm_delete.html'
    success_url = reverse_lazy('student-list')
