from django.db import models

class TrainingData(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    academic_pressure = models.FloatField(null=True, blank=True)
    work_pressure = models.FloatField(null=True, blank=True)
    cgpa = models.FloatField(null=True, blank=True)
    study_satisfaction = models.FloatField(null=True, blank=True)
    job_satisfaction = models.FloatField(null=True, blank=True)
    sleep_duration = models.CharField(max_length=50, null=True, blank=True)
    dietary_habits = models.CharField(max_length=50, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    suicidal_thoughts = models.CharField(max_length=10, null=True, blank=True)
    work_study_hour = models.FloatField(null=True, blank=True)
    financial_stress = models.FloatField(null=True, blank=True)
    family_history_mental_illness = models.CharField(max_length=10, null=True, blank=True)
    depression = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.gender} - {self.city} - {self.depression}"