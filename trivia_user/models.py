from django.db import models
from authenctication.models import User
import uuid
from django.utils.translation import gettext_lazy as text_lazy


# Create your models here.
class TriviaUser(models.Model):
    class UserType(models.TextChoices):
        HOST = "Host", text_lazy("Host")
        PARTICIPANT = "Participant", text_lazy("Participant")

    tu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="question id")
    trivia_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=20,
        choices = UserType.choices,
        default=UserType.PARTICIPANT,
        help_text="type of the trivia user"
    )
    date_created = models.DateTimeField(auto_now_add=True)

