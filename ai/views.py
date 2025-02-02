import csv
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CSVUploadForm
from .models import TrainingData


class ImportCSVView(FormView):
    template_name = 'ai/import_csv.html'  # Template que será renderizado
    form_class = CSVUploadForm  # Formulário para upload do CSV
    success_url = reverse_lazy('import_csv')  # URL para redirecionamento após o sucesso

    def form_valid(self, form):
        csv_file = form.cleaned_data.get('csv_file')

        # Verifica se o arquivo possui a extensão .csv
        if not csv_file.name.endswith('.csv'):
            messages.error(self.request, 'O arquivo enviado não é um CSV.')
            return self.form_invalid(form)

        # Função auxiliar para converter valores vazios em None
        def safe_cast(value, cast_func):
            if isinstance(value, str):
                value = value.strip()
            return cast_func(value) if value != '' else None

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            imported_count = 0  # Contador de registros importados com sucesso
            error_ids = []  # Lista para armazenar os IDs dos registros que geraram erro

            for row in reader:
                # Obtem o valor do ID e o trata separadamente, pois é obrigatório
                row_id_raw = row.get('id', '').strip()
                if not row_id_raw:
                    error_ids.append("ID não informado")
                    continue

                try:
                    row_id = int(row_id_raw)
                except Exception as e:
                    error_ids.append(f"ID inválido ({row_id_raw})")
                    continue

                try:
                    TrainingData.objects.update_or_create(
                        id=row_id,
                        defaults={
                            'gender': safe_cast(row.get('gender', ''), lambda x: x),
                            'age': safe_cast(row.get('age', ''), float),
                            'city': safe_cast(row.get('city', ''), lambda x: x),
                            'profession': safe_cast(row.get('profession', ''), lambda x: x),
                            'academic_pressure': safe_cast(row.get('academic_pressure', ''), float),
                            'work_pressure': safe_cast(row.get('work_pressure', ''), float),
                            'cgpa': safe_cast(row.get('cgpa', ''), float),
                            'study_satisfaction': safe_cast(row.get('study_satisfaction', ''), float),
                            'job_satisfaction': safe_cast(row.get('job_satisfaction', ''), float),
                            'sleep_duration': safe_cast(row.get('sleep_duration', ''), lambda x: x),
                            'dietary_habits': safe_cast(row.get('dietary_habits', ''), lambda x: x),
                            'degree': safe_cast(row.get('degree', ''), lambda x: x),
                            'suicidal_thoughts': safe_cast(row.get('suicidal_thoughts', ''), lambda x: x),
                            'work_study_hour': safe_cast(row.get('work_study_hour', ''), float),
                            'financial_stress': safe_cast(row.get('financial_stress', ''), float),
                            'family_history_mental_illness': safe_cast(row.get('family_history_mental_illness', ''),
                                                                       lambda x: x),
                            'depression': safe_cast(row.get('depression', ''), int),
                        }
                    )
                    imported_count += 1
                except Exception as e:
                    error_ids.append(str(row_id))

            if error_ids:
                messages.error(
                    self.request,
                    f"Ocorreu erro ao importar os registros com ID(s): {', '.join(error_ids)}."
                )
            messages.success(
                self.request,
                f"Arquivo CSV importado com sucesso! {imported_count} registros foram importados."
            )
        except Exception as e:
            messages.error(self.request, f"Ocorreu um erro ao processar o arquivo: {e}")

        return super().form_valid(form)
