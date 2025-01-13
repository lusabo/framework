from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'  # nome do template para exibir a lista
    context_object_name = 'courses'     # nome usado no template para referenciar a lista

class CourseCreateView(CreateView):
    model = Course
    fields = ['description']  # campos do modelo que serão exibidos no formulário
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')  # para onde redirecionar após criar

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['description']
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

