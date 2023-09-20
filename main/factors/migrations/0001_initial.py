# Generated by Django 4.2.3 on 2023-09-20 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Factors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("plases", models.CharField(max_length=100, verbose_name="Место")),
                (
                    "time",
                    models.TimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Время выполнения привычки",
                    ),
                ),
                ("action", models.CharField(max_length=100, verbose_name="Действие")),
                (
                    "associated_habit",
                    models.CharField(max_length=100, verbose_name="Связанная привычка"),
                ),
                (
                    "frequency",
                    models.IntegerField(default=1, verbose_name="Периодичность"),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "execution_time",
                    models.TimeField(
                        default="00:03", verbose_name="Время на выполнение"
                    ),
                ),
                (
                    "published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
            ],
            options={
                "verbose_name": "Фактор",
                "verbose_name_plural": "Факторы",
            },
        ),
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sign_pleasant_habit",
                    models.CharField(max_length=100, verbose_name="Признак привычки"),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(default=True, verbose_name="Приятная привычка"),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]