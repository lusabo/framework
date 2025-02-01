import base64
import io
import os

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")  # usar um backend que não abre janela de interface
import matplotlib.pyplot as plt

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_score
import pickle

from .forms import StudentForm
from .models import City, Student


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
    form_class = StudentForm
    template_name = 'student/form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/confirm_delete.html'
    success_url = reverse_lazy('student-list')

class EvaluationMetricsView(LoginRequiredMixin, TemplateView):
    """
    Classe que gera métricas como Curva ROC, Matriz de Confusão, Precisão, etc.
    e exibe em um template HTML.
    """
    template_name = 'metrics/evaluation_metrics.html'

    def get(self, request, *args, **kwargs):
        # 1. Carregar o pipeline treinado (model.pkl)
        model_path = os.path.join(settings.BASE_DIR, 'ai/model.pkl')
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