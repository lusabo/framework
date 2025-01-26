from django.db import migrations


def add_dietary_habits(apps, schema_editor):
    DietaryHabits = apps.get_model('enrollment', 'DietaryHabits')  # Substitua 'your_app_name' pelo nome do seu app
    habits = [
        "Healthy",
        "Moderate",
        "Others",
        "Unhealthy",
    ]
    for habit in habits:
        DietaryHabits.objects.create(name=habit)


def remove_dietary_habits(apps, schema_editor):
    DietaryHabits = apps.get_model('enrollment', 'DietaryHabits')  # Substitua 'your_app_name' pelo nome do seu app
    habits = [
        "Healthy",
        "Moderate",
        "Others",
        "Unhealthy",
    ]
    for habit in habits:
        DietaryHabits.objects.filter(name=habit).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0003_auto_20250126_1243'),
    ]

    operations = [
        migrations.RunPython(add_dietary_habits, remove_dietary_habits),
    ]
