import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
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

class ExportStudentsCSV(View):
    def get(self, request, *args, **kwargs):
        # Configura a resposta HTTP com o tipo CSV e o cabeçalho para download
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'

        writer = csv.writer(response)

        # Escreve a linha de cabeçalho conforme a estrutura desejada
        writer.writerow([
            'id',
            'gender',
            'age',
            'city',
            'profession',
            'academic_pressure',
            'work_pressure',
            'cgpa',
            'study_satisfaction',
            'job_satisfaction',
            'sleep_duration',
            'dietary_habits',
            'degree',
            'suicidal_thoughts',
            'work_study_hour',
            'financial_stress',
            'family_history_mental_illness'
        ])

        # Recupera todos os estudantes
        students = Student.objects.all()

        for student in students:
            writer.writerow([
                student.id,
                student.gender,
                student.age,
                str(student.city),
                str(student.profession),
                student.academic_pressure,
                student.work_pressure,
                student.cgpa,
                student.study_satisfaction,
                student.job_satisfaction,
                str(student.sleep_duration),
                str(student.dietary_habits),
                str(student.degree),
                student.suicidal_thoughts_display,
                student.work_study_hour,
                student.financial_stress,
                student.family_history_display
            ])

        return response