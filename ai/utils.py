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
    from django.conf import settings  # se precisar pegar caminhos do settings

    # Carregar o pipeline treinado
    model_path = 'model/model.pkl'  # Ajuste o path de acordo com seu projeto
    with open(model_path, 'rb') as file:
        pipeline = pickle.load(file)

    # Montar os dados de entrada conforme as colunas que foram usadas no treino
    data = {
        "gender": student.gender,                      # string
        "age": student.age,                            # int (ou None)
        "profession": student.profession.name,         # string
        "academic_pressure": student.academic_pressure,# int
        "work_pressure": student.work_pressure,        # int
        "cgpa": student.cgpa,                          # float
        "study_satisfaction": student.study_satisfaction,   # int
        "job_satisfaction": student.job_satisfaction,       # int
        "sleep_duration": student.sleep_duration.name,       # string
        "dietary_habits": student.dietary_habits.name,       # string
        "degree": student.degree.name,                       # string
        # Aqui usamos "Yes"/"No", pois definimos no CSV da mesma forma
        "suicidal_thoughts": "Yes" if student.suicidal_thoughts else "No",
        "work_study_hour": student.work_study_hour,          # int
        "financial_stress": student.financial_stress,        # int
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
