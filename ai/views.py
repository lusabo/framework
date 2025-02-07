import base64
import csv
import io
import os

import matplotlib
import numpy as np
import pandas as pd
from django.shortcuts import render

from .train_model import ModelTrainer

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from django.conf import settings

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_score
import pickle

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CSVUploadForm
from .models import TrainingData


class TrainModelView(TemplateView):
    template_name = 'ai/train_model.html'

    def post(self, request, *args, **kwargs):
        try:
            # Chama o método estático da classe ModelTrainer que realiza o treinamento
            metrics = ModelTrainer.train()
            messages.success(request, "Treinamento concluído com sucesso!")
        except Exception as e:
            metrics = None
            messages.error(request, f"Erro durante o treinamento: {str(e)}")
        # Renderiza o template passando as métricas obtidas (ou None em caso de erro)
        return render(request, self.template_name, {'metrics': metrics})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inicialmente, as métricas estão vazias
        context['metrics'] = None
        return context


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


class EvaluationMetricsView(LoginRequiredMixin, TemplateView):
    """
    Classe que gera métricas como Curva ROC, Matriz de Confusão, Precisão, etc.
    e exibe em um template HTML.
    """
    template_name = 'ai/metrics.html'

    def get(self, request, *args, **kwargs):
        # 1. Carregar o pipeline treinado (model.pkl)
        model_path = os.path.join(settings.BASE_DIR, 'model/model.pkl')
        with open(model_path, 'rb') as f:
            pipeline = pickle.load(f)

        # 2. Carregar o dataset (exemplo) para teste
        data_path = os.path.join(settings.BASE_DIR, 'ai/student_depression.csv')
        df = pd.read_csv(data_path)

        # Remover colunas que não foram usadas no treino
        target_column = "depression"
        meta_columns = ["id", "city"]
        df = df.drop(columns=meta_columns)

        # Separar X e y
        X = df.drop(columns=[target_column])
        y = df[target_column]

        # Split de treino e teste (mesmo random_state do treino, se quiser reproduzir)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Prever com o pipeline
        y_pred = pipeline.predict(X_test)
        y_prob = pipeline.predict_proba(X_test)[:, 1]

        # Métricas
        confusion = confusion_matrix(y_test, y_pred)
        prec = precision_score(y_test, y_pred)

        # Curva ROC
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)

        # -----------------------------------------------
        #    GRÁFICO 1: CURVA ROC
        # -----------------------------------------------
        plt.figure(figsize=(5, 4))
        plt.plot(fpr, tpr, color='red', label=f'ROC curve (area = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='blue', linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Curva ROC')
        plt.legend(loc="lower right")

        # Converter para base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        roc_image_png = buf.getvalue()
        roc_image_base64 = base64.b64encode(roc_image_png).decode('utf-8')
        plt.close()

        # -----------------------------------------------
        #    GRÁFICO 2: MATRIZ DE CONFUSÃO
        # -----------------------------------------------
        plt.figure(figsize=(5, 4))
        plt.matshow(confusion, cmap='Blues')
        plt.title('Matriz de Confusão', pad=15)
        plt.colorbar()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

        # Colocar valores nas células
        for (i, j), value in np.ndenumerate(confusion):
            plt.text(j, i, f"{value}", ha='center', va='center')

        buf2 = io.BytesIO()
        plt.savefig(buf2, format='png')
        buf2.seek(0)
        cm_image_png = buf2.getvalue()
        cm_image_base64 = base64.b64encode(cm_image_png).decode('utf-8')
        plt.close()

        # Preparar o contexto para o template
        context = {
            "precision": round(prec, 3),
            "roc_image_base64": roc_image_base64,
            "cm_image_base64": cm_image_base64,
        }

        return self.render_to_response(context)
