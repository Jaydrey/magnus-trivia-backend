# Generated by Django 4.1.3 on 2022-12-04 09:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("trivia", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "q_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="question id",
                    ),
                ),
                (
                    "question",
                    models.CharField(
                        max_length=500, verbose_name="question description"
                    ),
                ),
                (
                    "correct_choice",
                    models.UUIDField(blank=True, verbose_name="correct choice"),
                ),
                (
                    "choices",
                    models.CharField(
                        max_length=1000, null=True, verbose_name="choiced questions"
                    ),
                ),
                (
                    "answered_correctly",
                    models.BooleanField(
                        default=False, verbose_name="correctly answered"
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "trivia_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trivia.triviagroup",
                    ),
                ),
            ],
        ),
    ]
