# Generated by Django 4.1.3 on 2022-12-04 09:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TriviaGroup",
            fields=[
                (
                    "t_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="question id",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="group title")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]