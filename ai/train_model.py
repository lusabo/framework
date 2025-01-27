import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, matthews_corrcoef
)

# 1. Carregando o dataset
df = pd.read_csv('/Users/ctw00874/workspace/framework/ai/student_depression.csv')


# -----------------------------------------------------------
#    EXEMPLO DE CABEÇALHO ESPERADO EM student_depression.csv
#
#    id, gender, age, city, profession, academic_pressure,
#    work_pressure, cgpa, study_satisfaction, job_satisfaction,
#    sleep_duration, dietary_habits, degree, suicidal_thoughts,
#    work_study_hour, financial_stress, family_history_mental_illness,
#    depression
# -----------------------------------------------------------

# 2. Definindo target e removendo colunas que não serão usadas
target_column = "depression"
meta_columns = ["id", "city"]  # Por exemplo, se não quiser usar 'city' como feature

df = df.drop(columns=meta_columns)

# Separamos X e y
X = df.drop(columns=[target_column])
y = df[target_column]

# 3. Identificar colunas categóricas e numéricas
# Ajuste conforme seu dataset real:
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
# Ex.: [age, academic_pressure, work_pressure, cgpa, study_satisfaction,
#       job_satisfaction, work_study_hour, financial_stress]

# 4. Criar transformações para numéricas e categóricas
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

# 6. Split de treino e teste
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

print("\n==== Avaliação do Modelo ====")
print(f"AUC: {auc:.3f}")
print(f"Acurácia: {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1: {f1:.3f}")
print(f"MCC: {mcc:.3f}")

# 9. Salvar o pipeline inteiro (pré-processador + modelo)
model_filename = "model.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(model_pipeline, file)

print(f"\nPipeline completo salvo em: {model_filename}")