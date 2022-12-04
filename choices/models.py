from django.db import models
import uuid

from question.models import Question

# Create your models here.
class Choice(models.Model):
    c_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="question id",)
    choice = models.CharField(verbose_name="choice description", max_length=300)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    