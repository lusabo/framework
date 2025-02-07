from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from .forms import StudentForm
from .models import City, Student


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


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
    form_class = StudentForm
    template_name = 'student/form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/confirm_delete.html'
    success_url = reverse_lazy('student-list')
