import matplotlib

matplotlib.use("Agg")
from django.views.generic import TemplateView
from sklearn.metrics import confusion_matrix, precision_score
import pandas as pd

from ai.services.base_evaluation import BaseModelEvaluation
from ai.services import utils
from ai.models import TrainingData


class EvaluationMetricsView(BaseModelEvaluation, TemplateView):
    template_name = 'ai/metrics.html'

    def get(self, request, *args, **kwargs):
        pipeline = self.load_model()

        # Carregar e preparar os dados a partir do banco de dados
        qs = TrainingData.objects.all().values()
        df = pd.DataFrame(list(qs))

        # Remover colunas de metadados (caso existam)
        df = df.drop(columns=["id", "city"], errors='ignore')

        target_column = "depression"

        # Dividir os dados em treino e teste utilizando a função utilitária
        X_train, X_test, y_train, y_test = utils.split_data(
            df, target_column, stratify=df[target_column]
        )

        # Realizar predições e calcular as métricas
        y_pred = pipeline.predict(X_test)
        y_prob = pipeline.predict_proba(X_test)[:, 1]

        conf_matrix = confusion_matrix(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        roc_image_base64 = utils.generate_roc_plot(y_test, y_prob)
        cm_image_base64 = utils.generate_confusion_matrix_plot(conf_matrix)

        context = {
            "precision": round(prec, 3),
            "roc_image_base64": roc_image_base64,
            "cm_image_base64": cm_image_base64,
        }

        return self.render_to_response(context)
