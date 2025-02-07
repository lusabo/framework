from django.conf import settings
import os, pickle

class BaseModelEvaluation:
    model_filename = os.path.join(settings.MODEL_DIR, 'model.pkl')

    def load_model(self):
        with open(self.model_filename, 'rb') as f:
            return pickle.load(f)