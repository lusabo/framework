import os
import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, matthews_corrcoef
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Importa o model que representa a tabela de dados
from .models import TrainingData


class ModelTrainer:
    @staticmethod
    def train():
        # 1. Carregar os dados da tabela TrainingData do banco de dados
        # Converte o QuerySet em uma lista de dicionários para criar um DataFrame
        qs = TrainingData.objects.all().values()
        df = pd.DataFrame(list(qs))

        # Exemplo de cabeçalho esperado na tabela TrainingData:
        # id, gender, age, city, profession, academic_pressure,
        # work_pressure, cgpa, study_satisfaction, job_satisfaction,
        # sleep_duration, dietary_habits, degree, suicidal_thoughts,
        # work_study_hour, financial_stress, family_history_mental_illness,
        # depression

        # 2. Definir target e remover colunas que não serão usadas como features
        target_column = "depression"
        meta_columns = ["id", "city"]  # Colunas que servem apenas de metadados

        # Caso alguma coluna não exista, errors='ignore' evita erros
        df = df.drop(columns=meta_columns, errors='ignore')

        # Separar X (features) e y (target)
        X = df.drop(columns=[target_column])
        y = df[target_column]

        # 3. Identificar colunas categóricas e numéricas
        categorical_cols = [
            "gender",
            "profession",
            "sleep_duration",
            "dietary_habits",
            "degree",
            "suicidal_thoughts",
            "family_history_mental_illness"
        ]
        numerical_cols = list(set(X.columns) - set(categorical_cols))

        # 4. Criar transformações para colunas numéricas e categóricas
        numeric_transformer = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

        categorical_transformer = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ])

        preprocessor = ColumnTransformer([
            ("num", numeric_transformer, numerical_cols),
            ("cat", categorical_transformer, categorical_cols)
        ])

        # 5. Montar o Pipeline final (pré-processamento + modelo)
        model_pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=200, solver="liblinear"))
        ])

        # 6. Dividir os dados em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # 7. Treinar (fit) o pipeline
        model_pipeline.fit(X_train, y_train)

        # 8. Avaliar o modelo
        y_pred = model_pipeline.predict(X_test)
        y_pred_proba = model_pipeline.predict_proba(X_test)[:, 1]

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        mcc = matthews_corrcoef(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred_proba)

        # Organiza os dados de avaliação
        metrics = {
            "AUC": round(auc, 3),
            "Acurácia": round(accuracy, 3),
            "Precision": round(precision, 3),
            "Recall": round(recall, 3),
            "F1": round(f1, 3),
            "MCC": round(mcc, 3)
        }

        # 9. Salvar o pipeline (pré-processador + modelo) no diretório "model"
        model_dir = "model"
        os.makedirs(model_dir, exist_ok=True)
        model_filename = os.path.join(model_dir, "model.pkl")

        with open(model_filename, "wb") as file:
            pickle.dump(model_pipeline, file)

        metrics["model_path"] = model_filename

        # Retorna as métricas e o caminho do pipeline salvo
        return metrics
