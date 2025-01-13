from django.db import models

class Student(models.Model):

    GENDER_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro")
    ]

    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    def __str__(self):
        return self.name

class Course(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, help_text="Ex.: 2025.1")

    def __str__(self):
        return f"{self.student.name} - {self.course.description} - {self.semester}"

class Socioeconomic(models.Model):

    MARITAL_STATUS_CHOICES = [
        ("Solteiro", "Solteiro"),
        ("Casado", "Casado"),
        ("Divorciado", "Divorciado"),
        ("Viúvo", "Viúvo"),
    ]

    TRANSPORTATION_CHOICES = [
        ("Carro", "Carro"),
        ("Transporte público", "Transporte público"),
        ("Caminhada", "Caminhada"),
        ("Bicicleta", "Bicicleta"),
        ("Outros", "Outros"),
    ]

    enrollment = models.OneToOneField("Enrollment", on_delete=models.CASCADE)
    marital_status = models.CharField(
        max_length=50,
        choices=MARITAL_STATUS_CHOICES
    )
    children = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    mode_transportation = models.CharField(
        max_length=50,
        choices=TRANSPORTATION_CHOICES
    )
    household_size = models.PositiveIntegerField()
    annual_household_income = models.FloatField()

    def __str__(self):
        return f"Socioeconomic for {self.enrollment}"


