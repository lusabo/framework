from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Escolha o arquivo CSV", required=True)
