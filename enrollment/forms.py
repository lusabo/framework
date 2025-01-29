from django import forms
from .models import Student

GENDER_CHOICES = [
    ('Male', 'Masculino'),
    ('Female', 'Feminino')
]

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'name', 'date_birth', 'gender', 'city', 'profession', 'academic_pressure', 'work_pressure', 'cgpa',
            'study_satisfaction', 'job_satisfaction', 'sleep_duration', 'dietary_habits', 'degree',
            'suicidal_thoughts', 'work_study_hour', 'financial_stress', 'family_history_mental_illness'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-select'}),
            'academic_pressure': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5', 'step': '1'}),
            'work_pressure': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5', 'step': '1'}),
            'cgpa': forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'class': 'form-control'}),
            'study_satisfaction': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5', 'step': '1'}),
            'job_satisfaction': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '4', 'step': '1'}),
            'work_study_hour': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '12', 'step': '1'}),
            'financial_stress': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5', 'step': '1'}),
            'suicidal_thoughts': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'family_history_mental_illness': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'city': forms.Select(attrs={'class': 'form-select'}),
            'profession': forms.Select(attrs={'class': 'form-select'}),
            'sleep_duration': forms.Select(attrs={'class': 'form-select'}),
            'dietary_habits': forms.Select(attrs={'class': 'form-select'}),
            'degree': forms.Select(attrs={'class': 'form-select'}),
        }
