from django.db import models
import uuid

from trivia.models import TriviaGroup

# Create your models here.
class Question(models.Model):
    q_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="question id",)
    question = models.CharField(max_length=500, verbose_name="question description", )
    trivia_id=models.ForeignKey(TriviaGroup, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True, help_text="date the question was posted")
    # answered_correctly = models.BooleanField(verbose_name="correctly answered", default=False)

    def __str__(self):
        return f"{self.question}"

    def get_choices(self):
        return self.choice_set.all()
        