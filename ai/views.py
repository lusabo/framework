# views.py
import csv
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CSVUploadForm
from .models import TrainingData  # ou o nome do seu model


class ImportCSVView(FormView):
    template_name = 'ai/import_csv.html'  # Nome do template que será renderizado
    form_class = CSVUploadForm  # Formulário para upload do CSV
    success_url = reverse_lazy('import_csv')  # URL para redirecionar após o sucesso

    def form_valid(self, form):
        csv_file = form.cleaned_data.get('csv_file')

        # Verifica se o arquivo possui a extensão .csv
        if not csv_file.name.endswith('.csv'):
            messages.error(self.request, 'O arquivo enviado não é um CSV.')
            return self.form_invalid(form)

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            imported_count = 0  # Contador de registros importados

            for row in reader:
                TrainingData.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'gender': row['gender'],
                        'age': float(row['age']),
                        'city': row['city'],
                        'profession': row['profession'],
                        'academic_pressure': float(row['academic_pressure']),
                        'work_pressure': float(row['work_pressure']),
                        'cgpa': float(row['cgpa']),
                        'study_satisfaction': float(row['study_satisfaction']),
                        'job_satisfaction': float(row['job_satisfaction']),
                        'sleep_duration': row['sleep_duration'],
                        'dietary_habits': row['dietary_habits'],
                        'degree': row['degree'],
                        'suicidal_thoughts': row['suicidal_thoughts'],
                        'work_study_hour': float(row['work_study_hour']),
                        'financial_stress': float(row['financial_stress']),
                        'family_history_mental_illness': row['family_history_mental_illness'],
                        'depression': int(row['depression']),
                    }
                )
                imported_count += 1

            messages.success(
                self.request,
                f"Arquivo CSV importado com sucesso! {imported_count} registros foram importados."
            )
        except Exception as e:
            messages.error(self.request, f"Ocorreu um erro ao processar o arquivo: {e}")

        return super().form_valid(form)
