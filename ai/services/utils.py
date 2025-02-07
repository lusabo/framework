import base64
import io
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from django.conf import settings
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split


def generate_depression_risk(student):
    """
    Calcula a probabilidade de depressão para um estudante com base em um pipeline
    (pré-processamento + modelo) treinado.

    Args:
        student (Student): Objeto do modelo Student (Django).

    Returns:
        float: Probabilidade de depressão (percentual entre 0 e 100).
    """
    import pickle
    import pandas as pd

    # Carregar o pipeline treinado
    model_path = os.path.join(settings.MODEL_DIR, 'model.pkl')
    with open(model_path, 'rb') as file:
        pipeline = pickle.load(file)

    # Montar os dados de entrada conforme as colunas que foram usadas no treino
    data = {
        "gender": student.gender,  # string
        "age": student.age,  # int (ou None)
        "profession": student.profession.name,  # string
        "academic_pressure": student.academic_pressure,  # int
        "work_pressure": student.work_pressure,  # int
        "cgpa": student.cgpa,  # float
        "study_satisfaction": student.study_satisfaction,  # int
        "job_satisfaction": student.job_satisfaction,  # int
        "sleep_duration": student.sleep_duration.name,  # string
        "dietary_habits": student.dietary_habits.name,  # string
        "degree": student.degree.name,  # string
        # Aqui usamos "Yes"/"No", pois definimos no CSV da mesma forma
        "suicidal_thoughts": "Yes" if student.suicidal_thoughts else "No",
        "work_study_hour": student.work_study_hour,  # int
        "financial_stress": student.financial_stress,  # int
        # Também "Yes"/"No" conforme a col. family_history_mental_illness no CSV
        "family_history_mental_illness": (
            "Yes" if student.family_history_mental_illness else "No"
        ),
    }

    # Converter o dicionário em DataFrame
    df = pd.DataFrame([data])

    # Chamar o pipeline para fazer toda a transformação e predição
    probability = pipeline.predict_proba(df)[:, 1]  # Probabilidade da classe "1"

    # Retornar como percentual
    return probability[0] * 100  # ex.: 73.5%


def split_data(df, target_column, test_size=0.2, random_state=42, stratify=None):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=stratify)

def generate_roc_plot(y_test, y_prob):
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(5, 4))
    plt.plot(fpr, tpr, color='red', label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='blue', linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Curva ROC')
    plt.legend(loc="lower right")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    return image_base64


def generate_confusion_matrix_plot(confusion):
    plt.figure(figsize=(5, 4))
    plt.matshow(confusion, cmap='Blues')
    plt.title('Matriz de Confusão', pad=15)
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    for (i, j), value in np.ndenumerate(confusion):
        plt.text(j, i, f"{value}", ha='center', va='center')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    return image_base64
