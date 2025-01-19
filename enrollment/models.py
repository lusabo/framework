from django.db import models

class Course(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Student(models.Model):

    GENDER_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro")
    ]

    MARITAL_STATUS_CHOICES = [
        ("Solteiro", "Solteiro"),
        ("Casado", "Casado"),
        ("Divorciado", "Divorciado"),
        ("Viúvo", "Viúvo"),
    ]

    TRANSPORTATION_CHOICES = [
        ("Carro", "Carro"),
        ("Transporte público", "Transporte público"),
        ("A pé", "A pé"),
        ("Bicicleta", "Bicicleta"),
        ("Outros", "Outros"),
    ]

    DEFAULT_RISK = [
        ("Baixo", "Baixo"),
        ("Médio", "Médio"),
        ("Alto", "Alto"),
    ]

    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    enrollment_number = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marital_status = models.CharField(
        max_length=15,
        choices=MARITAL_STATUS_CHOICES
    )
    children = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    mode_transportation = models.CharField(
        max_length=30,
        choices=TRANSPORTATION_CHOICES
    )
    household_size = models.PositiveIntegerField()
    annual_household_income = models.FloatField()
    defaulter = models.BooleanField(default=False)
    default_risk = models.CharField(
        max_length=5,
        choices=DEFAULT_RISK,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name