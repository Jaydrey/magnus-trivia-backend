# Generated by Django 4.1.3 on 2022-12-05 15:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("question", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Choice",
            fields=[
                (
                    "c_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="question id",
                    ),
                ),
                (
                    "choice",
                    models.CharField(max_length=300, verbose_name="choice description"),
                ),
                (
                    "is_correct",
                    models.BooleanField(
                        default=False, help_text="choice correct or not"
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "question_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="question.question",
                    ),
                ),
            ],
        ),
    ]
