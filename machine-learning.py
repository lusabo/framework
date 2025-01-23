import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, matthews_corrcoef, roc_curve
)

# Métodos auxiliares
def get_columns_with_nulls(data):
    columns_with_nulls = data.columns[data.isnull().any()].tolist()
    return columns_with_nulls

############ PROGRAMA PRINCIPAL ############

# Carregando o dataframe
df = pd.read_csv('student_depression.csv')

# Classificando as colunas
target_column = 'Depression'
meta_columns = ['id', 'City']
feature_columns = [col for col in df.columns if col not in meta_columns + [target_column]]
categorical_columns = df[feature_columns].select_dtypes(include=['object', 'category']).columns
numerical_columns = df[feature_columns].select_dtypes(include=['int64', 'float64']).columns.tolist()

# Removendo colunas meta
df = df.drop(columns=meta_columns)

# Imputar Valores Ausentes
columns_with_nulls = get_columns_with_nulls(df)
for column in columns_with_nulls:
    print("\nImputing missing data for column: {}".format(column))
    df[column] = df[column].fillna(df[column].median())

# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=categorical_columns)

# Normalizando as colunas numéricas
scaler = StandardScaler()
df_encoded[numerical_columns] = scaler.fit_transform(df_encoded[numerical_columns])

# Separar dados de treinamento e teste
X = df_encoded.drop(columns=[target_column])  # Features
y = df_encoded[target_column]  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Treinar o modelo (regressão logística)
model = LogisticRegression(max_iter=200, solver='liblinear')
model.fit(X_train, y_train)

# Avaliar o modelo
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # Probabilidades para a classe positiva

# Calcular métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
mcc = matthews_corrcoef(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)

# Imprimir métricas

print("\nAvaliação do Modelo:")
print(f"AUC: {auc:.3f}")
print(f"Acurácia (CA): {accuracy:.3f}")
print(f"F1: {f1:.3f}")
print(f"Prec: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"MCC: {mcc:.3f}")


model_filename = 'model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

print(f"\nModelo salvo em: {model_filename}")