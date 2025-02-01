from django.db import models

class TrainingData(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.FloatField()
    city = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    academic_pressure = models.FloatField()
    work_pressure = models.FloatField()
    cgpa = models.FloatField()
    study_satisfaction = models.FloatField()
    job_satisfaction = models.FloatField()
    sleep_duration = models.CharField(max_length=50)
    dietary_habits = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    suicidal_thoughts = models.CharField(max_length=10)
    work_study_hour = models.FloatField()
    financial_stress = models.FloatField()
    family_history_mental_illness = models.CharField(max_length=10)
    depression = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.gender} - {self.city} - {self.depression}"