from django.urls import path
from .views import ImportCSVView, TrainModelView, EvaluationMetricsView

urlpatterns = [
    path('importar-csv/', ImportCSVView.as_view(), name='import_csv'),
    path('treinar-modelo/', TrainModelView.as_view(), name='train_model'),
    path('metricas/', EvaluationMetricsView.as_view(), name='metrics'),
]
