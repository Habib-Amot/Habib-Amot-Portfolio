from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.question)
        
    def was_created_recently(self):
        today = timezone.now()
        return today - datetime.timedelta(days=1) <= self.created_at <= today


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
