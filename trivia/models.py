from django.db import models
import uuid

# Create your models here.
class TriviaGroup(models.Model):
    t_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="question id",)
    title = models.CharField(verbose_name="group title", max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
