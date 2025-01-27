from django.db import models
from datetime import date
from ai.utils import generate_depression_risk

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SleepDuration(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DietaryHabits(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Degree(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    date_birth = models.DateField()
    gender = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='students')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='students')
    academic_pressure = models.IntegerField()
    work_pressure = models.IntegerField()
    cgpa = models.FloatField()
    study_satisfaction = models.IntegerField()
    job_satisfaction = models.IntegerField()
    sleep_duration = models.ForeignKey(SleepDuration, on_delete=models.CASCADE, related_name='students')
    dietary_habits = models.ForeignKey(DietaryHabits, on_delete=models.CASCADE, related_name='students')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='students')
    suicidal_thoughts = models.BooleanField()
    work_study_hour = models.IntegerField()
    financial_stress = models.IntegerField()
    family_history_mental_illness = models.BooleanField()
    risk_of_depression = models.FloatField(editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.risk_of_depression:
            self.risk_of_depression = generate_depression_risk(self)
        super().save(*args, **kwargs)

    @property
    def age(self):
        """Calcula a idade do estudante com base na data de nascimento."""
        if self.date_birth:
            today = date.today()
            return (
                    today.year - self.date_birth.year - ((today.month, today.day) < (self.date_birth.month, self.date_birth.day))
            )
        return None

    @property
    def suicidal_thoughts_display(self):
        return "Yes" if self.suicidal_thoughts else "No"

    @property
    def family_history_display(self):
        return "Yes" if self.family_history_mental_illness else "No"

def __str__(self):
        return self.name