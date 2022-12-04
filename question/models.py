from django.db import models
import uuid

from trivia.models import TriviaGroup

# Create your models here.
class Question(models.Model):
    q_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="question id",)
    question = models.CharField(max_length=500, verbose_name="question description", )
    trivia_id=models.ForeignKey(TriviaGroup, on_delete=models.CASCADE)
    correct_choice=models.UUIDField(verbose_name="correct choice",blank=True)
    # microservice field
    choices=models.CharField(max_length=1000, verbose_name="choiced questions", null=True)
    answered_correctly = models.BooleanField(verbose_name="correctly answered", default=False)
    date_created=models.DateTimeField(auto_now_add=True)

