from sklearn.metrics import confusion_matrix, precision_score

def evaluate_model(pipeline, X_test, y_test):
    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]
    confusion = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    # Outros cálculos de métricas, se necessário

    return {
        "y_pred": y_pred,
        "y_prob": y_prob,
        "confusion": confusion,
        "precision": precision,
    }
