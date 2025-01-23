from django.db import models

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
    financial_strees = models.IntegerField()
    family_history_mental_illness = models.BooleanField()
    risk_of_drepession = models.FloatField()

    def __str__(self):
        return self.name