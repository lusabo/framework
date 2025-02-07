from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from ai.services.train_model import ModelTrainer


class TrainModelView(TemplateView):
    template_name = 'ai/train_model.html'

    def post(self, request, *args, **kwargs):
        try:
            metrics = ModelTrainer.train()
            messages.success(request, "Treinamento concluído com sucesso!")
        except Exception as e:
            metrics = None
            messages.error(request, f"Erro durante o treinamento: {str(e)}")
        return render(request, self.template_name, {'metrics': metrics})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['metrics'] = None
        return context
