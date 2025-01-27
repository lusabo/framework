import pickle
import pandas as pd

def generate_depression_risk(student):
    """
    Calcula a probabilidade de depressão para um estudante com base em um modelo de IA treinado.

    Args:
        student (Student): Objeto do modelo Student.

    Returns:
        float: Probabilidade de depressão (percentual entre 0 e 100).
    """

    from enrollment.models import Student

    # Carregar o modelo treinado
    model_path = 'ai/model/model.pkl'  # Caminho para o modelo treinado
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Criar os dados de entrada (features) para o modelo
    data = {
        'gender': student.gender,
        'age': student.age,
        'profession': student.profession.name,
        'academic_pressure': student.academic_pressure,
        'work_pressure': student.work_pressure,
        'cgpa': student.cgpa,
        'study_satisfaction': student.study_satisfaction,
        'job_satisfaction': student.job_satisfaction,
        'sleep_duration': student.sleep_duration.name,
        'dietary_habits': student.dietary_habits.name,
        'degree': student.degree.name,
        'suicidal_thoughts': student.suicidal_thoughts_display,
        'work_study_hour': student.work_study_hour,
        'financial_strees': student.financial_stress,
        'family_history_mental_illness': student.family_history_display
    }

    # Converter para um DataFrame
    df = pd.DataFrame([data])

    # Certifique-se de que os dados estejam alinhados com as features do modelo
    # Ajuste as colunas, normalização ou one-hot encoding, se necessário

    # Fazer a previsão
    probability = model.predict_proba(df)[:, 1]  # Probabilidade da classe positiva (depressão)

    # Retornar como percentual
    return probability[0] * 100  # Percentual
